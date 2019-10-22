from django.test import TestCase
from model_mommy import mommy


class HistoryTest(TestCase):

    def setUp(self):
        self.history = mommy.make('History')

    def test_history(self):
        self.assertEqual(str(self.history), str(self.history.first_time))


class LaunchFailureDetailsTest(TestCase):

    def setUp(self):
        self.launch_failure_detail = mommy.make('LaunchFailureDetails')

    def test_launch_failure_detail(self):
        self.assertEqual(str(self.launch_failure_detail), str(self.launch_failure_detail.time))


class LaunchesTest(TestCase):

    def setUp(self):
        self.launches = mommy.make('Launches')

    def test_launches(self):
        self.assertEqual(str(self.launches), str(self.launches.flight_number))