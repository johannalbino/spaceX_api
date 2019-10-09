from rest_framework import serializers
from core.models import Ships


class ShipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ships
        fields = ('__all__')