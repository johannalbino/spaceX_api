import requests


class ConsumptionAPI(object):

    def __init__(self):
        self.req_api = requests.get('https://api.spacexdata.com/v3/launches/83/')
        self.req = {}

    def create_dict(self, name, dic):
        lis = []
        _dic = {}
        for a in dic:
            lis.append({str(name): a})
        return lis

    def search_all(self):
        req_api_all = self.req_api
        req_api_json = req_api_all.json()

        for a, b in req_api_json.items():
            if type(b) is list:
                lis = self.create_dict(a, b)
                self.req.update({str(a): lis})
            else:
                self.req.update({str(a): b})

        return dict(self.req)
