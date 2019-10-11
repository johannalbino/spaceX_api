from collections import OrderedDict
import requests


class ConsumptionAPI(object):

    def __init__(self):
        self.req_api = requests.get('https://api.spacexdata.com/v3/launches/83/')
        self.req = {}

    def create_order_dict(self, dic):
        _field = OrderedDict()
        _field_images = OrderedDict()
        _list_field = []
        for a, b in dic.items():
            if type(b) is not dict:
                if 'flickr_images' in a:
                    for c in b:
                        _field_images[a] = c
                        _list_field.append(_field_images)
                    _field[a] = _list_field
                else:
                    _field[a] = b
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

    def search_all(self):
        req_api_all = self.req_api
        req_api_json = req_api_all.json()

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
