from rest_framework import serializers
from core.models import Timeline


class TimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = ['webcast_liftoff', 'go_for_prop_loading', 'rp1_loading', 'stage1_lox_loading', 'stage2_lox_loading',
                  'engine_chill', 'prelaunch_checks', 'propellant_pressurization', 'go_for_launch', 'ignition', 'liftoff',
                  'maxq', 'meco', 'stage_sep', 'second_stage_ignition', 'seco1', 'dragon_separation', 'dragon_solar_deploy',
                  'dragon_bay_door_deploy', 'webcast_launch', 'payload_deploy_1', 'payload_deploy_2', 'center_core_boostback',
                  'first_stage_entry_burn', 'first_stage_landing_burn']