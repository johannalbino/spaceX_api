from django.test import TestCase
from model_mommy import mommy


class MissionTest(TestCase):

    def setUp(self):
        self.mission_id = mommy.make('Mission')

    def test_mission(self):
        self.assertEqual(str(self.mission_id), str(self.mission_id.mission_id))