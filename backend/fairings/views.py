from rest_framework import viewsets
from rest_framework.response import Response

from rocket.models import Fairings
from .serializer import FairingsSerializer


class FairingsViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Fairings.objects.all()
    serializer_class = FairingsSerializer

    def get_queryset(self):
        return Fairings.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Fairings.objects.all()
        serializer = FairingsSerializer(queryset, many=True)
        return Response(serializer.data)