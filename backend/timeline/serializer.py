from rest_framework import serializers
from core.models import Timeline


class TimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = ('__all__')