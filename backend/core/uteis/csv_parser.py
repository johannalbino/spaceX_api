from pandas import DataFrame


class CsvParser(object):

    def __init__(self):
        self.__list_values = []

    def generate_csv(self, values_csv):

        if values_csv.__len__() >= 1:
            for val in values_csv:
                dic_values = {}
                values_del = ['id', 'ships', 'telemetry', 'launch_site', 'launch_success', 'launch_failure_details',
                              'links', 'timeline', 'crew']
                for d in values_del:
                    del val[d]
                for a, b in val.items():
                    if a == 'rocket':
                        for c, d in b.items():
                            if c != 'first_stage' and c != 'second_stage' and c != 'fairings':
                                dic_values[c] = d
                    elif a == 'mission_id':
                        for c in b:
                            dic_values[a] = c['mission_id']
                    else:
                        dic_values[a] = b
                self.__list_values.append(dic_values)

        df = DataFrame(self.__list_values)
        return df
