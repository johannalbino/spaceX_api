from rest_framework import serializers
from .models import (Payloads,
                     OrbitParams,
                     Customers,
                     Norad)
from rocket.models import SecondStage


class OrbitParamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrbitParams
        fields = ['reference_system', 'regime', 'longitude', 'semi_major_axis_km', 'eccentricity', 'periapsis_km',
                  'apoapsis_km', 'inclination_deg', 'period_min', 'lifespan_years', 'epoch', 'mean_motion',
                  'raan', 'arg_of_pericenter', 'mean_anomaly']


class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ['customers']


class NoradSerializer(serializers.ModelSerializer):

    class Meta:
        model = Norad
        fields = ['norad_id']


class PayloadsSerializer(serializers.ModelSerializer):

    norad_id = NoradSerializer(many=True)
    customers = CustomersSerializer(many=True)
    orbit_params = OrbitParamsSerializer(many=False)

    class Meta:
        model = Payloads
        fields = ['payload_id', 'norad_id', 'cap_serial', 'reused', 'customers', 'nationality', 'manufacturer',
                  'payload_type', 'payload_mass_kg', 'payload_mass_lbs', 'orbit', 'orbit_params', 'mass_returned_kg',
                  'mass_returned_lbs', 'flight_time_sec', 'cargo_manifest', 'uid']


class SecondStageSerializer(serializers.ModelSerializer):

    payloads = PayloadsSerializer(many=True)
    class Meta:
        model = SecondStage
        fields = ['block', 'payloads']