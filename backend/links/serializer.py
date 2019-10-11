from rest_framework import serializers
from core.models import Links
from .models import FlickrImages


class FlickrImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlickrImages
        fields = ['flickr_images']


class LinksSerializer(serializers.ModelSerializer):

    flickr_images = FlickrImagesSerializer(many=True)

    class Meta:
        model = Links
        fields = ['mission_patch', 'mission_patch_small', 'reddit_campaign', 'reddit_launch', 'reddit_recovery',
                  'reddit_media', 'presskit', 'article_link', 'wikipedia', 'video_link', 'youtube_id', 'flickr_images']

    def create_flickr(self, flickr_images, links):
        for flickr in flickr_images:
            _relation_data = FlickrImages.objects.create(**flickr)
            links.flickr_images.add(_relation_data)

    def create(self, validated_data):
        flickr_images = validated_data['flickr_images']
        del validated_data['flickr_images']

        links = Links.objects.create(**validated_data)

        self.create_flickr(flickr_images, links)

        return links
