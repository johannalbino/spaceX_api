from rest_framework import serializers
from .models import (Rocket,
                     FirstStage,
                     SecondStage,
                     Fairings)
from first_stage.serializer import FirstStageSerializer
from second_stage.serializer import SecondStageSerializer
from fairings.serializer import FairingsSerializer


class RocketSerializer(serializers.ModelSerializer):
    first_stage = FirstStageSerializer(many=False)
    second_stage = SecondStageSerializer(many=False)
    fairings = FairingsSerializer(many=False)

    class Meta:
        model = Rocket
        fields = ['rocket_id', 'rocket_name', 'rocket_type', 'first_stage', 'second_stage', 'fairings']

    def verify_relations_in_relations(self, data_validate, _serializers):

        verify = False
        validated_data = []
        for _, value in data_validate.items():
            if type(value) is list:
                for _value in value:
                    try:
                        for _, value_items in _value.items():
                            verify = True
                        validated_data.append(data_validate)
                    except AttributeError:
                        verify = False

        if verify is True:
            id_relation = _serializers().create(validated_data[0])
            return id_relation
        return verify

    def create_relations_one_to_one(self, *args):
        rocket = Rocket

        _serializers = [FirstStageSerializer, SecondStageSerializer, FairingsSerializer]
        models = [FirstStage, SecondStage, Fairings]
        campos_pk = [rocket.first_stage, rocket.second_stage, rocket.fairings]

        relations = list(zip(models, campos_pk, args[0], _serializers))

        if args.__len__() > 0:
            for rel in relations:
                rel_list = list(rel)
                verify_relations = self.verify_relations_in_relations(rel[2], rel[3])
                if verify_relations is False:
                    _relation_data = rel_list[0].objects.create(**rel[2])
                    rel_list[1] = _relation_data
                else:
                    rel_list[1] = verify_relations

    def create(self, validated_data):
        try:
            _data_one = []

            _field_one_to_one = ['first_stage', 'second_stage', 'fairings']

            for one_to_one in _field_one_to_one:
                _data_one.append(validated_data[one_to_one])
                del validated_data[one_to_one]

            rocket = Rocket.objects.create(**validated_data)
            self.create_relations_one_to_one(_data_one)

            return rocket
        except Exception as e:
            print(f'Erro no Rocket Serializer:\n{e}')
            return False

