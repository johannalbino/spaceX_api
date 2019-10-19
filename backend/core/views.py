from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .uteis import ConsumptionApi
from .models import Launches, LaunchFailureDetails
from .serializer import LaunchesSerializer, LaunchFailureDetailsSerializer


class LaunchFailureDetailsViewSet(viewsets.ModelViewSet):
    queryset = LaunchFailureDetails.objects.all()
    serializer_class = LaunchFailureDetailsSerializer


class LaunchesViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """
    queryset = Launches.objects.all()
    serializer_class = LaunchesSerializer
    consumption = ConsumptionApi.ConsumptionAPI()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Launches.objects.all()
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
            return Response(status=status.HTTP_201_CREATED)

        except:
            return Response({'msg': 'Error trying to save'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['get'], detail=False)
    def latest_consumption(self, request):
        id_flight_number = self.consumption.get_latest_launche()
        queryset = Launches.objects.filter(flight_number=id_flight_number)
        serializer = LaunchesSerializer(queryset, many=True)
        return Response({'Results': serializer.data})

    @action(methods=['get'], detail=False)
    def next_launche(self, request):
        id_flight_number = self.consumption.get_next_launche()
        queryset = Launches.objects.filter(flight_number=id_flight_number)
        serializer = LaunchesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return Response({'msg': 'CREATE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        return Response({'msg': 'UPDATE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        return Response({'msg': 'DELETE option not available for this application.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)