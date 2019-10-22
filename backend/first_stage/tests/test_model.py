from django.test import TestCase
from model_mommy import mommy


class CoresTest(TestCase):

    def setUp(self):
        self.cores = mommy.make('Cores')

    def test_cores(self):
        self.assertEqual(str(self.cores), str(self.cores.core_serial))


class FirstStageTest(TestCase):

    def setUp(self):
        self.first_stage = mommy.make('FirstStage')

    def test_first_stage(self):
        self.assertEqual(str(self.first_stage), str(self.first_stage.cores))