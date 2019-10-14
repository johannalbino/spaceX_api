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
            id_relation.save()
            return id_relation
        return False

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

    def create_relations_many_to_many(self, launches, *args, **kwargs):
        models = [Mission, Ships]
        campos_pk = [launches.mission_id, launches.ships]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                at = rel[0].objects.create(**rel[2][0])
                rel[1].add(at)

    def validated_content(self, contents):
        valid = False

        if contents is None:
            valid = True
        return valid

    def create(self, validated_data):
        validated_data = self.consumption.search_all()
        _fields_many_to_many = ['mission_id', 'ships']
        _fields_one_to_one = ['launch_site', 'rocket', 'telemetry', 'links', 'timeline']

        launches = Launches

        _data_many = []
        _data_one = []

        for many_to_many in _fields_many_to_many:
            _data_many.append(validated_data[many_to_many])
            del validated_data[many_to_many]

        if _fields_one_to_one.__len__() > 1:
            for one_to_one in _fields_one_to_one:
                _data_one.append(validated_data[one_to_one])
                del validated_data[one_to_one]

            launches = Launches.objects.create(**validated_data)
            self.create_relations_one_to_one(_data_one)
            launches.save()
        """
        else:
            _field_one = validated_data[str(_fields_one_to_one[0])]
            del validated_data[str(_fields_one_to_one[0])]
            one_to_one_model_field = ModelFieldOne.objects.create(**_field_one)
            launches = launches.objects.create(**validated_data)
            launches._field_one = one_to_one_model_field
            launches.save()
        """

        self.create_relations_many_to_many(launches, _data_many)
        launches = Launches.objects.create(**validated_data)

        return launches
