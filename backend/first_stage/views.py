from rest_framework import viewsets
from rest_framework.response import Response
from .models import Cores
from rocket.models import FirstStage
from .serializer import (FirstStageSerializer,
                         CoresSerializer)


class FirstStageViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = FirstStage.objects.all()
    serializer_class = FirstStageSerializer

    def get_queryset(self):
        return FirstStage.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = FirstStage.objects.all()
        serializer = FirstStageSerializer(queryset, many=True)
        return Response(serializer.data)


class CoresViewSet(viewsets.ModelViewSet):
    queryset = Cores.objects.all()
    serializer_class = CoresSerializer