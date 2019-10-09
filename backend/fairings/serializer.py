from rest_framework import serializers
from rocket.models import Fairings


class FairingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fairings
        fields = ('__all__')