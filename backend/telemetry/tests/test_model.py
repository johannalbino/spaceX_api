from django.test import TestCase
from model_mommy import mommy


class TelemetryTest(TestCase):

    def setUp(self):
        self.telemetry = mommy.make('Telemetry')

    def test_telemetry(self):
        self.assertEqual(str(self.telemetry), str(self.telemetry.flight_club))
