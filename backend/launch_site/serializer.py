from rest_framework import serializers
from core.models import LaunchSite


class LaunchSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = LaunchSite
        fields = ['site_id', 'site_name', 'site_name_long']

