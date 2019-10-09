from rest_framework import viewsets
from rest_framework.response import Response

from .models import Launches
from .serializer import LaunchesSerializer


class LaunchesViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Launches.objects.all()
    serializer_class = LaunchesSerializer

    def get_queryset(self):
        return Launches.objects.all()

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
