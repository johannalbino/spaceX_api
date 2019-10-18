from collections import OrderedDict
import requests


class ConsumptionAPI(object):

    def __init__(self):
        self.req_api = requests.get('https://api.spacexdata.com/v3/launches/')
        self.req = {}

    def create_order_dict(self, dic):
        _field = OrderedDict()
        _field_images = OrderedDict()
        _list_field = []
        for a, b in dic.items():
            if list is not type(b) is not dict:
                if 'flickr_images' in a:
                    for c in b:
                        _field_images[a] = c
                        _list_field.append(_field_images)
                    _field[a] = _list_field
                else:
                    _field[a] = b
            elif type(b) is dict:
                _field[a] = self.create_order_dict(b)
            else:
                _field[a] = self.create_list_order_dict(a, b)
        return _field

    def create_list_order_dict(self, key, lis):
        _list_field = []
        _dict_filed = OrderedDict()
        if lis.__len__() > 0:
            if type(lis[0]) is dict:
                for a in lis:
                    b = self.create_order_dict(a)
                    _list_field.append(b)
                return _list_field
            else:
                for a in lis:
                    _dict_filed[key] = a
                    _list_field.append(_dict_filed)
                return _list_field

        return _list_field

    @classmethod
    def get_latest_launche(cls):
        req_api = requests.get('https://api.spacexdata.com/v3/launches/latest?pretty=true')
        info_latest_api = req_api.json()
        flight_number = info_latest_api['flight_number']
        return flight_number

    @classmethod
    def removing_special_characters(cls, data_dic):

        for key, value in data_dic.items():
            _split_field_key = key.split('-')
            if _split_field_key.__len__() > 1:
                _new_key = ''
                for i in _split_field_key:
                    _new_key += str(i)
                del data_dic[key]
                data_dic.update({str(_new_key): value})
        return data_dic

    def search_all(self):
        req_api_all = self.req_api
        req_api_json = req_api_all.json()
        list_req_api = []

        for req_api in req_api_json:
            try:
                for a, b in req_api.items():
                    if a == 'timeline':
                        b_atual = ConsumptionAPI.removing_special_characters(req_api[a])
                        del req_api[a]
                        req_api.update({str(a): b_atual})
                        break
                    else:
                        pass
            except Exception as e:
                #print(f'Erro ao tentar remover os caracteres especiais!')
                pass

            for a, b in req_api.items():
                if a == 'launch_failure_details':
                    field_exclusive = False
                    break
                field_exclusive = True
            if field_exclusive:
                req_api.update({'launch_failure_details': None})

            for a, b in req_api.items():
                if type(b) is dict:
                    b = self.create_order_dict(b)
                    self.req.update({str(a): b})
                elif type(b) is list:
                    b = self.create_list_order_dict(a, b)
                    self.req.update({str(a): b})
                else:
                    self.req.update({str(a): b})
            list_req_api.append(dict(self.req))
        return list_req_api