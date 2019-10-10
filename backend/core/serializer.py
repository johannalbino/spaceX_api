from rest_framework.serializers import ModelSerializer
from .models import Launches
from mission.serializer import MissionSerializer
from rocket.serializer import RocketSerializer
from ships.serializer import ShipsSerializer
from telemetry.serializer import TelemetrySerializer
from launch_site.serializer import LaunchSiteSerializer
from links.serializer import LinksSerializer
from timeline.serializer import TimelineSerializer
from mission.models import Mission
from rocket.models import Rocket
from ships.models import Ships
from telemetry.models import Telemetry
from launch_site.models import LaunchSite
from links.models import Links
from timeline.models import Timeline


class LaunchesSerializer(ModelSerializer):

    mission_id = MissionSerializer(many=True)
    rocket = RocketSerializer(many=False, read_only=True)
    ships = ShipsSerializer(many=True, read_only=True)
    telemetry = TelemetrySerializer(many=False, read_only=True)
    launch_site = LaunchSiteSerializer(many=False)
    links = LinksSerializer(many=False, read_only=True)
    timeline = TimelineSerializer(many=False, read_only=True)

    class Meta:
        model = Launches
        fields = ['flight_number', 'mission_name', 'mission_id', 'launch_year', 'launch_date_unix', 'launch_date_utc',
                  'launch_date_local', 'is_tentative', 'tentative_max_precision', 'tbd', 'launch_window', 'rocket',
                  'ships', 'telemetry', 'launch_site', 'launch_success', 'links', 'details',
                  'upcoming', 'static_fire_date_utc', 'static_fire_date_unix', 'timeline', 'crew']

    def create_relations_many_to_many(self, launche, *args, **kwargs):
        models = [Mission]
        campos_pk = [launche.mission_id]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                at = rel[0].objects.create(**rel[2][0])
                rel[1].add(at)
        elif kwargs.__len__() > 0:
            pass

    def create_relations_one_to_one(self, launche, *args, **kwargs):
        models = []
        campos_pk = [launche.launch_site]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                at = rel[0].objects.create(**rel[2])
                rel[1] = at
        elif kwargs.__len__() > 0:
            pass

    def create(self, validated_data):

        _data_many = []
        _data_one = []

        launche = Launches

        _field_many_to_many = ['mission_id']
        _field_one_to_one = ['launch_site']

        for many_to_many in _field_many_to_many:
            _data_many.append(validated_data[many_to_many])
            del validated_data[many_to_many]

        if _field_one_to_one.__len__() > 1:
            for one_to_one in _field_one_to_one:
                _data_one.append(validated_data[one_to_one])
                del validated_data[one_to_one]
            self.launche = Launches.objects.create(**validated_data)
            self.create_relations_one_to_one(self.launche, _data_one)

        elif _field_one_to_one.__len__() is 1:

            _one_field = validated_data[str(_field_one_to_one[0])]
            del validated_data[str(_field_one_to_one[0])]

            self.launche = Launches.objects.create(**validated_data)
            at = LaunchSite.objects.create(**_one_field)
            launche.launch_site = at

        launche = Launches.objects.create(**validated_data)
        self.create_relations_many_to_many(launche, _data_many)

        return launche
