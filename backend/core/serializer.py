from rest_framework import serializers
from .models import Launches
from mission.models import Mission


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ('__all__')


class LaunchesSerializer(serializers.ModelSerializer):

    #mission = MissionSerializer(many=False)

    class Meta:
        model = Launches
        fields = ('__all__')