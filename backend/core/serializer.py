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
from .uteis import ConsumptionApi


class LaunchesSerializer(ModelSerializer):

    consumption = ConsumptionApi.ConsumptionAPI()

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

    def verify_relations_in_relations(self, data_validate, _serializers):
        verify = False
        validated_data = []
        print(data_validate)

        try:
            for _, value in data_validate.items():
                try:
                    for _, value_items in value.items():
                        verify = True
                    validated_data.append(value)
                except AttributeError:
                    if type(value) is list:
                        verify = True
                    else:
                        verify = False
                    validated_data.append(value)
        except Exception as e:
            return False

        if verify is True:
            id_relation = _serializers().create(data_validate)
            id_relation.save()
            return id_relation
        return verify

    def create_relations_one_to_one(self, *args):
        launche = Launches

        models = [LaunchSite, Rocket, Telemetry, Links, Timeline]
        campos_pk = [launche.launch_site, launche.rocket, launche.telemetry, launche.links, launche.timeline]
        _serializers = [LaunchesSerializer, RocketSerializer, TelemetrySerializer, LinksSerializer, TimelineSerializer]

        relations = list(zip(models, campos_pk, args[0], _serializers))

        if args.__len__() > 0:
            for rel in relations:
                rel_list = list(rel)

                if rel[2] is None:
                    _relation_data = rel_list[0].objects.create()
                    rel_list[1] = _relation_data
                else:
                    verify_relations = self.verify_relations_in_relations(rel[2], rel[3])

                    if verify_relations is False:
                        _relation_data = rel_list[0].objects.create(**rel[2])
                        rel_list[1] = _relation_data
                    else:
                        rel_list[1] = verify_relations

    def create_mission(self, mission_id, launches):
        for mission in mission_id:
            _relation_data = Mission.objects.create(**mission)
            launches.mission_id.add(_relation_data)

    def create_ships(self, ships, launches):
        for shi in ships:
            _relation_data = Ships.objects.create(**shi)
            launches.ships.add(_relation_data)

    def validated_content(self,contents):
        valid = False

        if contents is None:
            valid = True
        return valid

    def create(self, validated_data):
        validated_data = self.consumption.search_all()
        _fields = ['mission_id', 'ships', 'launch_site', 'rocket', 'telemetry', 'links', 'timeline']
        _data = []
        _data_serializer = []

        mission_id = validated_data['mission_id']
        ships = validated_data['ships']
        launch_site = validated_data['launch_site']
        _data.append(launch_site)
        rocket = validated_data['rocket']
        _data.append(rocket)
        telemetry = validated_data['telemetry']
        _data.append(telemetry)
        links = validated_data['links']
        _data.append(links)
        timeline = validated_data['timeline']
        _data.append(timeline)

        for remove_fields in _fields:
            del validated_data[remove_fields]

        self.create_relations_one_to_one(_data)

        launches = Launches.objects.create(**validated_data)

        self.create_mission(mission_id, launches)
        self.create_ships(ships, launches)

        launches.save()
        return launches
