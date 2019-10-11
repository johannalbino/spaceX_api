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

    def verify_relations_in_relations(self, data_validate):
        verify = False
        validated_data = []
        for _, value in data_validate.items():
            try:
                for _, value_items in value.items():
                    verify = True
                validated_data.append(value)
            except AttributeError:
                verify = False

        if verify is True:
            id_relation_rocket = RocketSerializer().create(data_validate)
            return id_relation_rocket
        return verify


    def create_relations_many_to_many(self, launche, *args):
        models = [Mission, Ships]
        campos_pk = [launche.mission_id, launche.ships]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                _relation_data = rel[0].objects.create(**rel[2][0])
                rel[1].add(_relation_data)

    def create_relations_one_to_one(self, *args):
        launche = Launches

        models = [LaunchSite, Rocket, Telemetry, Links, Timeline]
        campos_pk = [launche.launch_site, launche.rocket, launche.telemetry, launche.links, launche.timeline]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                rel_list = list(rel)
                verify_relations = self.verify_relations_in_relations(rel[2])
                if verify_relations is False:
                    _relation_data = rel_list[0].objects.create(**rel[2])
                    rel_list[1] = _relation_data
                else:
                    rel_list[1] = verify_relations

    def create(self, validated_data):

        _data_many = []
        _data_one = []

        launche = Launches

        _field_many_to_many = ['mission_id', 'ships']
        _field_one_to_one = ['launch_site', 'rocket', 'telemetry', 'links', 'timeline']

        for many_to_many in _field_many_to_many:
            _data_many.append(validated_data[many_to_many])
            del validated_data[many_to_many]

        if _field_one_to_one.__len__() > 1:
            for one_to_one in _field_one_to_one:
                _data_one.append(validated_data[one_to_one])
                del validated_data[one_to_one]
            launche = Launches.objects.create(**validated_data)
            self.create_relations_one_to_one(_data_one)

        elif _field_one_to_one.__len__() is 1:

            _one_field = validated_data[str(_field_one_to_one[0])]
            del validated_data[str(_field_one_to_one[0])]

            self.launche = Launches.objects.create(**validated_data)
            _relation_data = LaunchSite.objects.create(**_one_field)
            launche.launch_site = _relation_data

        launche = Launches.objects.create(**validated_data)
        self.create_relations_many_to_many(launche, _data_many)
        launche.save()

        return launche
