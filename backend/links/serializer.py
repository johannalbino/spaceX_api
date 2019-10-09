from rest_framework import serializers
from core.models import Links


class LinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Links
        fields = ('__all__')