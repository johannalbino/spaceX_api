from rest_framework import viewsets, status
from rest_framework.response import Response
from .uteis import ConsumptionApi
from .models import Launches
from .serializer import LaunchesSerializer, CreateLaunchesSerializer


class LaunchesViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """
    queryset = Launches.objects.all()
    serializer_class = CreateLaunchesSerializer

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
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except:
            return Response({'msg': 'Erro ao salvar'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        serializer.save()