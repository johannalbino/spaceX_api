from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Ships
from .serializer import ShipsSerializer


class ShipsViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Ships.objects.all()
    serializer_class = ShipsSerializer

    def get_queryset(self):
        return Ships.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Ships.objects.all()
        serializer = ShipsSerializer(queryset, many=True)
        return Response(serializer.data)
