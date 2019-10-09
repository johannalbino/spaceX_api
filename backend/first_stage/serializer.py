from rest_framework import serializers
from rocket.models import FirstStage


class FirstStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirstStage
        fields = ('__all__')
