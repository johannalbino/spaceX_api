from rest_framework import viewsets
from rest_framework.response import Response

from core.models import LaunchSite
from .serializer import LaunchSiteSerializer


class LaunchSiteViewSet(viewsets.ModelViewSet):
    """
        A simple ViewSet for viewing and editing.
    """

    queryset = LaunchSite.objects.all()
    serializer_class = LaunchSiteSerializer

    def get_queryset(self):
        return LaunchSite.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Função para listar da forma que eu preciso quando for realizado um get no endpoint
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = LaunchSite.objects.all()
        serializer = LaunchSiteSerializer(queryset, many=True)
        return Response(serializer.data)
