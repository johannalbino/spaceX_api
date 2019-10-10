from rest_framework.serializers import ModelSerializer
from .models import Launches
from mission.serializer import MissionSerializer
from rocket.serializer import RocketSerializer
from ships.serializer import ShipsSerializer
from telemetry.serializer import TelemetrySerializer
from launch_site.serializer import LaunchSiteSerializer
from links.serializer import LinksSerializer
from timeline.serializer import TimelineSerializer


class LaunchesSerializer(ModelSerializer):

    mission_id = MissionSerializer(many=True, read_only=True)
    rocket = RocketSerializer(many=False, read_only=True)
    ships = ShipsSerializer(many=True, read_only=True)
    telemetry = TelemetrySerializer(many=False, read_only=True)
    launch_site = LaunchSiteSerializer(many=False, read_only=True)
    links = LinksSerializer(many=False, read_only=True)
    timeline = TimelineSerializer(many=False, read_only=True)

    class Meta:
        model = Launches
        fields = ['flight_number', 'mission_name', 'mission_id', 'launch_year', 'launch_date_unix', 'launch_date_utc',
                  'launch_date_local', 'is_tentative', 'tentative_max_precision', 'tbd', 'launch_window', 'rocket',
                  'ships', 'telemetry', 'launch_site', 'launch_success', 'links', 'details',
                  'upcoming', 'static_fire_date_utc', 'static_fire_date_unix', 'timeline', 'crew']


class CreateLaunchesSerializer(ModelSerializer):

    mission_id = MissionSerializer(many=True)
    rocket = RocketSerializer(many=False)
    ships = ShipsSerializer(many=True)
    telemetry = TelemetrySerializer(many=False)
    launch_site = LaunchSiteSerializer(many=False)
    links = LinksSerializer(many=False)
    timeline = TimelineSerializer(many=False)

    class Meta:
        model = Launches
        fields = ['flight_number', 'mission_name', 'mission_id', 'launch_year', 'launch_date_unix', 'launch_date_utc',
                  'launch_date_local', 'is_tentative', 'tentative_max_precision', 'tbd', 'launch_window', 'rocket',
                  'ships', 'telemetry', 'launch_site', 'launch_success', 'links', 'details',
                  'upcoming', 'static_fire_date_utc', 'static_fire_date_unix', 'timeline', 'crew']


