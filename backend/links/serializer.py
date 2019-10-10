from rest_framework import serializers
from core.models import Links
from .models import FlickrImages


class FlickrImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlickrImages
        fields = ['link_images']


class LinksSerializer(serializers.ModelSerializer):

    flickr_images = FlickrImagesSerializer(many=True)

    class Meta:
        model = Links
        fields = ['mission_patch', 'mission_patch_small', 'reddit_campaign', 'reddit_launch', 'reddit_recovery',
                  'reddit_media', 'presskit', 'article_link', 'wikipedia', 'video_link', 'youtube_id', 'flickr_images']