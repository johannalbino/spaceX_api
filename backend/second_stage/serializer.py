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

    def verify_relations_in_relations(self, data_validate, _serializers):

        verify = False
        validated_data = []
        for _, value in data_validate.items():
            if type(value) is list:
                for _value in value:
                    try:
                        for _, value_items in _value.items():
                            verify = True
                        validated_data.append(data_validate)
                    except AttributeError:
                        verify = False

        if verify is True:
            id_relation = _serializers().create(validated_data[0])
            return id_relation
        return verify

    def create_relations_one_to_one(self, *args):
        payloads = Payloads

        _serializers = [OrbitParamsSerializer]
        models = [OrbitParams]
        campos_pk = [payloads.orbit_params]

        relations = list(zip(models, campos_pk, args[0], _serializers))

        if args.__len__() > 0:
            for rel in relations:
                rel_list = list(rel)
                verify_relations = self.verify_relations_in_relations(rel[2], rel[3])
                if verify_relations is False:
                    _relation_data = rel_list[0].objects.create(**rel[2])
                    rel_list[1] = _relation_data
                else:
                    rel_list[1] = verify_relations

    def create_relations_many_to_many(self, payloads, *args):
        models = [Norad, Customers]
        campos_pk = [payloads.norad_id, payloads.customers]

        relations = list(zip(models, campos_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                if rel[2].__len__() == 0:
                    _relation_data = rel[0].objects.create()
                    rel[1].add(_relation_data)
                else:
                    _relation_data = rel[0].objects.create(**rel[2][0])
                    rel[1].add(_relation_data)

    def create(self, validated_data):
        try:
            _data_many = []
            _data_one = []

            _field_many_to_many = ['norad_id', 'customers']
            _field_one_to_one = ['orbit_params']

            for many_to_many in _field_many_to_many:
                _data_many.append(validated_data[many_to_many])
                del validated_data[many_to_many]

            if _field_one_to_one.__len__() > 1:
                for one_to_one in _field_one_to_one:
                    _data_one.append(validated_data[one_to_one])
                    del validated_data[one_to_one]
                _payloads = Payloads.objects.create(**validated_data)
                self.create_relations_one_to_one(_data_one)

            elif _field_one_to_one.__len__() is 1:
                try:
                    _one_field = validated_data[str(_field_one_to_one[0])]
                    del validated_data[str(_field_one_to_one[0])]
                    _payloads = Payloads.objects.create(**validated_data)

                    _relation_data = OrbitParams.objects.create(**_one_field)
                    _payloads.orbit_params = _relation_data
                except:
                    print('Erro ao salvar orbit_params\n')
            try:
                self.create_relations_many_to_many(_payloads, _data_many)
            except:
                print('Erro ao salvar norad_id ou customers!')

            _payloads.save()
            return _payloads
        except:
            return False


class SecondStageSerializer(serializers.ModelSerializer):

    payloads = PayloadsSerializer(many=True)

    class Meta:
        model = SecondStage
        fields = ['block', 'payloads']

    def verify_relations_in_relations(self, data_validate):

        verify = False
        for _, value in data_validate.items():
            if type(value) is list:
                for _value in value:
                    try:
                        for _, value_items in _value.items():
                            verify = True
                    except AttributeError:
                        verify = False
        return verify

    def create_relations_many_to_many(self, second_stage, *args):
        models = [Payloads]
        fields_pk = [second_stage.payloads]

        relations = list(zip(models, fields_pk, args[0]))

        if args.__len__() > 0:
            for rel in relations:
                verify_relations = self.verify_relations_in_relations(rel[2][0])
                if verify_relations is False:
                    _relation_data = rel[0].objects.create(**rel[2][0])
                    rel[1].add(_relation_data)
                else:
                    pay_data = PayloadsSerializer().create(rel[2][0])
                    rel[1].add(pay_data)

    def create(self, validated_data):
        try:
            _data_many = []
            _fields_many = ['payloads']

            for many_to_many in _fields_many:
                _data_many.append(validated_data[many_to_many])
                del validated_data[many_to_many]

            second_stage = SecondStage.objects.create(**validated_data)
            self.create_relations_many_to_many(second_stage, _data_many)

            return second_stage
        except:
           return False