from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Mission
from .serializer import MissionSerializer


class MissionViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def get_queryset(self):
        return Mission.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Mission.objects.all()
        serializer = MissionSerializer(queryset, many=True)
        return Response(serializer.data)
