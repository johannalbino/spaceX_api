from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .uteis import ConsumptionApi
from .models import Launches, LaunchFailureDetails
from .serializer import LaunchesSerializer, LaunchFailureDetailsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters


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
            queryset = Launches.objects.all().delete()
            serializer = LaunchesSerializer(queryset, many=True)

            data_req = self.consumption.search_all()
            for data in data_req:
                serializer = LaunchesSerializer().create(data)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer)
            return Response({'msg': 'Consumption successfully completed'},status=status.HTTP_201_CREATED)

        except:
            return Response({'msg': 'Error trying to save'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False)
    def latest_consumption(self, request):
        id_flight_number = self.consumption.get_latest_launche()
        queryset = Launches.objects.filter(flight_number=id_flight_number)
        serializer = LaunchesSerializer(queryset, many=True)
        return Response({'results': serializer.data})

    @action(methods=['get'], detail=False)
    def next_launche(self, request):
        id_flight_number = self.consumption.get_next_launche()
        queryset = Launches.objects.filter(flight_number=id_flight_number)
        serializer = LaunchesSerializer(queryset, many=True)
        return Response({'results': serializer.data})

    def create(self, request, *args, **kwargs):
        return Response({'msg': 'CREATE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        return Response({'msg': 'UPDATE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        return Response({'msg': 'DELETE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)