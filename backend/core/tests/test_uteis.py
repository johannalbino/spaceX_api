from django.test import TestCase
from core.uteis.ConsumptionApi import (
                                        ConsumptionAPI,
                                        OrderedDict
                                    )
# Create your tests here.


class ConsumptionTest(TestCase):

    def test_create_order_dict(self):
        self.assertEqual(
            ConsumptionAPI().create_order_dict({'Teste': 'um Dicionario'}),
            OrderedDict([('Teste', 'um Dicionario')])
        )

    def test_create_list_order_dict(self):
        self.assertEqual(
            ConsumptionAPI().create_list_order_dict('teste_lis', [{'Teste': 'um Dicionario'}]),
            [OrderedDict([('Teste', 'um Dicionario')])]
        )