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
                _relation_data = rel[0].objects.create(**rel[2])
                rel[1].add(_relation_data)

    def create(self, validated_data):
        try:
            _data_many = validated_data['cores']
            first_stage = FirstStage.objects.create()
            self.create_relations_many_to_many(first_stage, _data_many)
            return first_stage
        except:
           return False

