from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Telemetry
from .serializer import TelemetrySerializer


class TelemetryViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer

    def get_queryset(self):
        return Telemetry.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Telemetry.objects.all()
        serializer = TelemetrySerializer(queryset, many=True)
        return Response(serializer.data)
