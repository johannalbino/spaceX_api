from rest_framework import serializers
from core.models import Mission


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ('__all__')