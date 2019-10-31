from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .uteis import ConsumptionApi
from .models import Launches, LaunchFailureDetails, History
from .serializer import LaunchesSerializer, LaunchFailureDetailsSerializer, HistorySerializer
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .uteis.csv_parser import CsvParser
csv_parser = CsvParser()


class LaunchFailureDetailsViewSet(viewsets.ModelViewSet):
    queryset = LaunchFailureDetails.objects.all()
    serializer_class = LaunchFailureDetailsSerializer


class LaunchesFilter(filters.FilterSet):
    flight_number = filters.CharFilter(lookup_expr='icontains')
    mission_name = filters.CharFilter(lookup_expr='icontains')
    launch_year = filters.CharFilter(lookup_expr='icontains')
    launch_date_unix = filters.CharFilter(lookup_expr='icontains')
    launch_date_utc = filters.CharFilter(lookup_expr='icontains')
    is_tentative = filters.CharFilter(lookup_expr='icontains')
    launch_success = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Launches
        fields = ('flight_number', 'mission_name', 'launch_year', 'launch_date_unix', 'launch_date_utc',
                  'is_tentative', 'launch_success')


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class LaunchesViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """
    queryset = Launches.objects.all()
    serializer_class = LaunchesSerializer
    consumption = ConsumptionApi.ConsumptionAPI()
    pagination_class = StandardResultsSetPagination
    filterset_class = LaunchesFilter

    def get_queryset(self):
        return self.queryset

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = LaunchesSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = LaunchesSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def consumption_api(self, request):
        try:
            History.objects.all().delete()
            queryset = Launches.objects.all().delete()
            serializer = LaunchesSerializer(queryset, many=True)

            latest_launche = self.consumption.get_latest_launche()
            next_launche = self.consumption.get_next_launche()
            History.objects.create(first_time=False, latest_launche=latest_launche, next_launche=next_launche)

            data_req = self.consumption.search_all()
            for data in data_req:
                serializer = LaunchesSerializer().create(data)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer)
            return Response({'msg': 'Consumption successfully completed'},status=status.HTTP_201_CREATED)

        except:
            return Response({'msg': 'Error trying to save, check the api that is being consumed'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False)
    def latest_consumption(self, request):
        _id_flight = 1
        queryset = History.objects.all()
        serializer = HistorySerializer(queryset, many=True)

        if serializer.data.__len__() > 1:
            History.objects.all().delete()
        if serializer.data.__len__() < 1:
            History.objects.create(first_time=False, latest_launche=0, next_launche=0)
        if serializer.data.__len__() == 1:
            _id_flight = serializer.data[0]

        try:
            id_flight_number = self.consumption.get_latest_launche()
            History.objects.filter(id=_id_flight['id']).update(latest_launche=id_flight_number)
            queryset = Launches.objects.filter(flight_number=id_flight_number)
            serializer = LaunchesSerializer(queryset, many=True)
        except:
            queryset = Launches.objects.filter(flight_number=_id_flight['latest_launche'])
            serializer = LaunchesSerializer(queryset, many=True)

        return Response({'results': serializer.data})

    @action(methods=['get'], detail=False)
    def next_launche(self, request):
        _id_flight = 1
        queryset = History.objects.all()
        serializer = HistorySerializer(queryset, many=True)

        if serializer.data.__len__() > 1:
            History.objects.all().delete()
        if serializer.data.__len__() < 1:
            History.objects.create(first_time=False, latest_launche=0, next_launche=0)
        if serializer.data.__len__() == 1:
            _id_flight = serializer.data[0]

        try:
            id_flight_number = self.consumption.get_next_launche()
            History.objects.filter(id=_id_flight['id']).update(next_launche=id_flight_number)
            queryset = Launches.objects.filter(flight_number=id_flight_number)
            serializer = LaunchesSerializer(queryset, many=True)
        except:
            queryset = Launches.objects.filter(flight_number=_id_flight['next_launche'])
            serializer = LaunchesSerializer(queryset, many=True)

        return Response({'results': serializer.data})

    @action(methods=['get'], detail=False)
    def export_file(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = LaunchesSerializer(queryset, many=True)
        csv = csv_parser.generate_csv(serializer.data)
        response = HttpResponse(csv.to_csv(path_or_buf=None, sep=';'), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="launches.csv"'
        return response

    def create(self, request, *args, **kwargs):
        return Response({'msg': 'CREATE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        return Response({'msg': 'UPDATE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        return Response({'msg': 'DELETE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)