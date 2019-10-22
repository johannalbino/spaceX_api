from django.test import TestCase
from core.uteis.ConsumptionApi import (
                                        ConsumptionAPI,
                                        OrderedDict
                                    )
from model_mommy import mommy


class ConsumptionTest(TestCase):

    def setUp(self):
        self.order_dictionary = OrderedDict([('Teste', 'um Dicionario'),
                                             ('flickr_images', [OrderedDict([('flickr_images', 'abc')])]),
                                             ('umDicionario', OrderedDict([('oi', 'oi')])),
                                             ('lista', [OrderedDict([('lista', 'item1')])])
                                             ])
        self.list_order_dictionary = [OrderedDict([('Teste', 'um Dicionario')])]

    def test_create_order_dict(self):
        self.assertEqual(
            ConsumptionAPI().create_order_dict({'Teste': 'um Dicionario', 'flickr_images': ['abc'], 'umDicionario': {'oi': 'oi'}, 'lista': ['item1']}),
            self.order_dictionary
        )

    def test_create_list_order_dict(self):
        self.assertEqual(
            ConsumptionAPI().create_list_order_dict('teste_lis', [{'Teste': 'um Dicionario'}]),
            self.list_order_dictionary
        )
        self.assertEqual(
            ConsumptionAPI().create_list_order_dict('teste_lis', []),
            []
        )

    def test_get_latest_launche(self):
        self.assertEqual(
            type(ConsumptionAPI.get_latest_launche()),
            int
        )

    def test_removing_special_characters(self):
        self.assertEqual(
            ConsumptionAPI.removing_special_characters({'com-caracter': 'lista-2'}),
            {'comcaracter': 'lista-2'}
        )

    def test_next_launche(self):
        self.assertEqual(
            type(ConsumptionAPI.get_next_launche()),
            int
        )