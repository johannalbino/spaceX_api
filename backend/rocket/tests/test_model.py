from django.test import TestCase
from model_mommy import mommy


class RocketTest(TestCase):

    def setUp(self):
        self.rocket = mommy.make('Rocket')

    def test_rocket(self):
        self.assertEqual(str(self.rocket), str(self.rocket.rocket_id))