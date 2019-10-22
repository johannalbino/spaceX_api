from django.test import TestCase
from model_mommy import mommy


class OrbitParamsTest(TestCase):

    def setUp(self):
        self.orbit_params = mommy.make('OrbitParams')

    def test_orbit_params(self):
        self.assertEqual(str(self.orbit_params), str(self.orbit_params.reference_system))


class CustomersTest(TestCase):

    def setUp(self):
        self.customers = mommy.make('Customers')

    def test_customers(self):
        self.assertEqual(str(self.customers), str(self.customers.customers))


class NoradTest(TestCase):

    def setUp(self):
        self.norad = mommy.make('Norad')

    def test_norad(self):
        self.assertEqual(str(self.norad), str(self.norad.norad_id))


class PayloadsTest(TestCase):

    def setUp(self):
        self.payloads = mommy.make('Payloads')

    def test_payloads(self):
        self.assertEqual(str(self.payloads), str(self.payloads.payload_id))


class SecondStageTest(TestCase):

    def setUp(self):
        self.second_stage = mommy.make('SecondStage')

    def test_second_stage(self):
        self.assertEqual(str(self.second_stage), str(self.second_stage.block))