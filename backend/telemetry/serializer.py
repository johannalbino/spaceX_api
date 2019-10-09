from rest_framework import serializers
from core.models import Telemetry


class TelemetrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Telemetry
        fields = ('__all__')