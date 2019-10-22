from django.test import TestCase
from model_mommy import mommy


class LaunchSiteTest(TestCase):

    def setUp(self):
        self.launch_site = mommy.make('LaunchSite')

    def test_launch_site(self):
        self.assertEqual(str(self.launch_site), str(self.launch_site.site_id))