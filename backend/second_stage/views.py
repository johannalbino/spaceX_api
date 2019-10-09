from rest_framework import viewsets
from rest_framework.response import Response

from rocket.models import SecondStage
from .serializer import SecondStageSerializer


class SecondStageViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = SecondStage.objects.all()
    serializer_class = SecondStageSerializer

    def get_queryset(self):
        return SecondStage.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = SecondStage.objects.all()
        serializer = SecondStageSerializer(queryset, many=True)
        return Response(serializer.data)
