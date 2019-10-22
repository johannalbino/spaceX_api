from django.test import TestCase
from model_mommy import mommy


class FlickrImagesTest(TestCase):

    def setUp(self):
        self.flickr_images = mommy.make('FlickrImages')

    def test_flickr_images(self):
        self.assertEqual(str(self.flickr_images), str(self.flickr_images.flickr_images))


class LinksTest(TestCase):

    def setUp(self):
        self.links = mommy.make('Links')

    def test_links(self):
        self.assertEqual(str(self.links), str(self.links.mission_patch))