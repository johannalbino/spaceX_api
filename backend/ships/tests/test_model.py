from django.test import TestCase
from model_mommy import mommy


class ShipsTest(TestCase):

    def setUp(self):
        self.ships = mommy.make('Ships')

    def test_ships(self):
        self.assertEqual(str(self.ships), str(self.ships.ships))