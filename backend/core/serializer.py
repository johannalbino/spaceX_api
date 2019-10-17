from rest_framework.serializers import ModelSerializer
from .models import Launches, LaunchFailureDetails
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


class LaunchFailureDetailsSerializer(ModelSerializer):
    class Meta:
        model = LaunchFailureDetails
        fields = ['time', 'altitude', 'reason']


class LaunchesSerializer(ModelSerializer):

    consumption = ConsumptionApi.ConsumptionAPI()

    mission_id = MissionSerializer(many=True)
    rocket = RocketSerializer(many=False)
    ships = ShipsSerializer(many=True)
    telemetry = TelemetrySerializer(many=False)
    launch_site = LaunchSiteSerializer(many=False)
    links = LinksSerializer(many=False)
    timeline = TimelineSerializer(many=False)
    launch_failure_details = LaunchFailureDetailsSerializer(many=False)

    class Meta:
        model = Launches
        fields = ['id', 'flight_number', 'mission_name', 'mission_id', 'launch_year', 'launch_date_unix', 'launch_date_utc',
                  'launch_date_local', 'is_tentative', 'tentative_max_precision', 'tbd', 'launch_window', 'rocket',
                  'ships', 'telemetry', 'launch_site', 'launch_success', 'launch_failure_details', 'links', 'details',
                  'upcoming', 'static_fire_date_utc', 'static_fire_date_unix', 'timeline', 'crew']

    def verify_relations_in_relations(self, data_validate, _serializers):
        verify = []
        validated_data = []
        print(data_validate)

        try:
            for _, value in data_validate.items():
                try:
                    for _, value_items in value.items():
                        verify.append(True)
                    validated_data.append(value)
                except AttributeError:
                    if type(value) is list:
                        verify.append(True)
                    else:
                        verify.append(False)
                    validated_data.append(value)
        except Exception as e:
            return False

        if True in verify:
            id_relation = _serializers().create(data_validate)

            return id_relation
        return False

    def create_relations_one_to_one(self, _fields_one_to_one, *args):
        launche = Launches
        _data_one = []

        for one_to_one in _fields_one_to_one:
            try:
                _data_one.append(args[0][one_to_one])
                del args[0][one_to_one]
            except Exception as e:
                _data_one.append(None)

        models = [LaunchSite, Rocket, Telemetry, Links, Timeline, LaunchFailureDetails]
        campos_pk = [launche.launch_site, launche.rocket, launche.telemetry, launche.links, launche.timeline, launche.launch_failure_details]
        _serializers = [LaunchesSerializer, RocketSerializer, TelemetrySerializer, LinksSerializer, TimelineSerializer, LaunchFailureDetailsSerializer]

        relations = list(zip(models, campos_pk, _data_one, _serializers, _fields_one_to_one))
        launche = Launches.objects.create(**args[0])

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
                        if rel[4] == 'launch_site':
                            launche.launch_site = _relation_data
                        elif rel[4] == 'rocket':
                            launche.rocket = _relation_data
                        elif rel[4] == 'telemetry':
                            launche.telemetry = _relation_data
                        elif rel[4] == 'links':
                            launche.links = _relation_data
                        elif rel[4] == 'timeline':
                            launche.timeline = _relation_data
                        elif rel[4] == 'launch_failure_details':
                            launche.launch_failure_details = _relation_data
                        launche.save()
                    else:
                        if rel[4] == 'launch_site':
                            launche.launch_site = verify_relations
                        elif rel[4] == 'rocket':
                            launche.rocket = verify_relations
                        elif rel[4] == 'telemetry':
                            launche.telemetry = verify_relations
                        elif rel[4] == 'links':
                            launche.links = verify_relations
                        elif rel[4] == 'timeline':
                            launche.timeline = verify_relations
                        elif rel[4] == 'launch_failure_details':
                            launche.launch_failure_details = verify_relations
                        launche.save()

            return launche

    def create_relations_many_to_many(self, launches, *args, **kwargs):
        models = [Mission, Ships]
        campos_pk = [launches.mission_id, launches.ships]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                if rel[2].__len__() == 0:
                    at = rel[0].objects.create()
                else:
                    at = rel[0].objects.create(**rel[2][0])
                rel[1].add(at)

    def validated_content(self, contents):
        valid = False

        if contents is None:
            valid = True
        return valid

    def create(self, validated_data):
        _fields_many_to_many = ['mission_id', 'ships']
        _fields_one_to_one = ['launch_site', 'rocket', 'telemetry', 'links', 'timeline', 'launch_failure_details']

        launches = Launches

        _data_many = []
        _data_one = []

        for many_to_many in _fields_many_to_many:
            _data_many.append(validated_data[many_to_many])
            del validated_data[many_to_many]

        if _fields_one_to_one.__len__() > 1:
            launches = self.create_relations_one_to_one(_fields_one_to_one, validated_data)

        self.create_relations_many_to_many(launches, _data_many)
        return launches
