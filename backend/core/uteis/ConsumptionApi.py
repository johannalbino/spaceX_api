from collections import OrderedDict
import requests


class ConsumptionAPI(object):

    def __init__(self):
        self.req_api = requests.get('https://api.spacexdata.com/v3/launches/10/')
        self.req = {}

    def create_order_dict(self, dic):
        _field = OrderedDict()
        _field_images = OrderedDict()
        _list_field = []
        for a, b in dic.items():
            if type(b) is not dict and list:
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
                _field[a] = self.create_order_dict(b)
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

    def removing_special_characters(self, data_dic):

        for keys, value in data_dic.items():
            if type(value) is dict:
                for key, value_items in value.items():
                    _split_field_key = key.split('-')
                    if _split_field_key.__len__() > 1:
                        _new_key = ''
                        for i in _split_field_key:
                            _new_key += str(i)
                        value[_new_key] = value_items
                        del value[key]
        return data_dic

    def search_all(self):
        req_api_all = self.req_api
        req_api_json = req_api_all.json()

        teste = self.removing_special_characters(req_api_json)

        for a, b in req_api_json.items():
            if type(b) is dict:
                b = self.create_order_dict(b)
                self.req.update({str(a): b})
            elif type(b) is list:
                b = self.create_list_order_dict(a, b)
                self.req.update({str(a): b})
            else:
                self.req.update({str(a): b})


        return dict(self.req)
