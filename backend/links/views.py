from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Links
from .serializer import LinksSerializer


class LinksViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Links.objects.all()
    serializer_class = LinksSerializer

    def get_queryset(self):
        return Links.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Links.objects.all()
        serializer = LinksSerializer(queryset, many=True)
        return Response(serializer.data)