from rest_framework import serializers
from .models import Launches


class LaunchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Launches
        fields = ('__all__')