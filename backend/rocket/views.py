from rest_framework import viewsets
from rest_framework.response import Response

from .models import Rocket
from .serializer import RocketSerializer


class RocketViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer

    def get_queryset(self):
        return Rocket.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Rocket.objects.all()
        serializer = RocketSerializer(queryset, many=True)
        return Response(serializer.data)
