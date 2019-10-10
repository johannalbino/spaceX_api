from rest_framework import serializers
from .models import Rocket
from first_stage.serializer import FirstStageSerializer
from second_stage.serializer import SecondStageSerializer
from fairings.serializer import FairingsSerializer


class RocketSerializer(serializers.ModelSerializer):
    first_stage = FirstStageSerializer(many=False)
    second_stage = SecondStageSerializer(many=False)
    fairings = FairingsSerializer(many=False)

    class Meta:
        model = Rocket
        fields = ['rocket_my_id', 'rocket_name', 'rocket_type', 'first_stage', 'second_stage', 'fairings']
