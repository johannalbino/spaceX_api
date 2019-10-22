from django.test import TestCase
from model_mommy import mommy


class FairingsTest(TestCase):

    def setUp(self):
        self.fairings = mommy.make('Fairings')

    def test_fairings(self):
        self.assertEqual(str(self.fairings), str(self.fairings.reused))

