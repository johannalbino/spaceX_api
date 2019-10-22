from django.test import TestCase
from model_mommy import mommy


class TimelineTest(TestCase):

    def setUp(self):
        self.timeline = mommy.make('Timeline')

    def test_timeline(self):
        self.assertEqual(str(self.timeline), str(self.timeline.webcast_liftoff))