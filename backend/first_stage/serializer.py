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

    def create_relations_many_to_many(self, first_stage, *args):
        models = [Cores]
        fields_pk = [first_stage.cores]

        relations = list(zip(models, fields_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                if rel[2].__len__() == 0:
                    at = rel[0].objects.create()
                else:
                    at = rel[0].objects.create(**rel[2])
                rel[1].add(at)

    def create(self, validated_data):
        try:
            _data_many = validated_data['cores']
            del validated_data['cores']
            first_stage = FirstStage.objects.create(**validated_data)

            if _data_many.__len__() <= 1:
                data = Cores.objects.create(**_data_many[0])
                first_stage.cores.add(data)
            else:
                self.create_relations_many_to_many(first_stage, _data_many)
            return first_stage

        except Exception as e:
           return False

