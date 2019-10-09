from rest_framework import serializers
from .models import Rocket


class RocketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rocket
        fields = ('__all__')