from django.db import models

# Create your models here.


class FlickrImages(models.Model):
    link_images = models.CharField(max_length=300)

    def __str__(self):
        return self.link_images


class Links(models.Model):
    mission_patch = models.CharField(max_length=100, blank=True, null=True)
    mission_patch_small = models.CharField(max_length=100, blank=True, null=True)
    reddit_campaign = models.CharField(max_length=100, blank=True, null=True)
    reddit_launch = models.CharField(max_length=100, blank=True, null=True)
    reddit_recovery = models.CharField(max_length=100, blank=True, null=True)
    reddit_media = models.CharField(max_length=100, blank=True, null=True)
    presskit = models.CharField(max_length=100, blank=True, null=True)
    article_link = models.CharField(max_length=100, blank=True, null=True)
    wikipedia = models.CharField(max_length=100, blank=True, null=True)
    video_link = models.CharField(max_length=100, blank=True, null=True)
    youtube_id = models.CharField(max_length=100, blank=True, null=True)
    flickr_images = models.ManyToManyField(FlickrImages, blank=True)

    def __str__(self):
        return self.mission_patch + ' ' + self.mission_patch_small
