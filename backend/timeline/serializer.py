from rest_framework import serializers
from core.models import Timeline


class TimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = ['webcast_liftoff', 'go_for_prop_loading', 'rp1_loading', 'stage1_lox_loading', 'stage2_lox_loading',
                  'engine_chill', 'prelaunch_checks', 'propellant_pressurization', 'go_for_launch', 'ignition', 'liftoff',
                  'maxq', 'meco', 'stage_sep', 'second_stage_ignition', 'seco1', 'dragon_separation', 'dragon_solar_deploy',
                  'dragon_bay_door_deploy']