from django.db import models

# Create your models here.


class FlickrImages(models.Model):
    link_images = models.CharField(max_length=300)


class Links(models.Model):
    mission_patch = models.CharField(max_length=100)
    mission_patch_small = models.CharField(max_length=100)
    reddit_campaign = models.CharField(max_length=100)
    reddit_launch = models.CharField(max_length=100)
    reddit_recovery = models.CharField(max_length=100)
    reddit_media = models.CharField(max_length=100)
    presskit = models.CharField(max_length=100)
    article_link = models.CharField(max_length=100)
    wikipedia = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)
    youtube_id = models.CharField(max_length=100)
    flickr_images = models.ManyToManyField(FlickrImages)
