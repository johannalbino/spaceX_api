from rest_framework import serializers
from rocket.models import SecondStage


class SecondStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SecondStage
        fields = ('__all__')