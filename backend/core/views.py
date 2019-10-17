from rest_framework import viewsets, status
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

    def create(self, request, *args, **kwargs):

        try:
            consumption = ConsumptionApi.ConsumptionAPI()
            data_req = consumption.search_all()
            for data in data_req:
                serializer = LaunchesSerializer().create(data)
                #serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except:
            return Response({'msg': 'Erro ao salvar'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        queryset = Launches.objects.all().delete()
        serializer = LaunchesSerializer(queryset, many=True)
        return Response(status=status.HTTP_204_NO_CONTENT)