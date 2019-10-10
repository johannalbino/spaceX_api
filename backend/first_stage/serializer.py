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

    def create_cores(self, cores, first_stage):
        for cor in cores:
            data_cor = Cores.objects.create(**cor)
            first_stage.cores.add(data_cor)

    def create(self, validated_data):
        try:
            _data_many = ['cores']
            del validated_data[_data_many]
            first_stage = FirstStage.objects.create(**validated_data)
            self.create_cores(_data_many, first_stage)
            return first_stage
        except:
            return False

