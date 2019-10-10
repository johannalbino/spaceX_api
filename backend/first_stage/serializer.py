from rest_framework import serializers
from .models import Cores
from rocket.models import FirstStage


class CoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cores
        fields = ['core_serial', 'flight', 'block', 'gridfins', 'legs', 'reused', 'land_success', 'landing_intent',
                  'landing_type', 'landing_vehicle']


class FirstStageSerializer(serializers.ModelSerializer):

    cores = CoresSerializer(many=True)

    class Meta:
        model = FirstStage
        fields = ['cores']
