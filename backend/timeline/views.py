from rest_framework import viewsets
from rest_framework.response import Response

from core.models import Timeline
from .serializer import TimelineSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer

    def get_queryset(self):
        return Timeline.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = Timeline.objects.all()
        serializer = TimelineSerializer(queryset, many=True)
        return Response(serializer.data)
