from django.db import models

# Create your models here.


class FlickrImages(models.Model):
    flickr_images = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.link_images


class Links(models.Model):
    mission_patch = models.TextField( blank=True, null=True)
    mission_patch_small = models.TextField(blank=True, null=True)
    reddit_campaign = models.TextField(blank=True, null=True)
    reddit_launch = models.TextField(blank=True, null=True)
    reddit_recovery = models.TextField(blank=True, null=True)
    reddit_media = models.TextField(blank=True, null=True)
    presskit = models.TextField(blank=True, null=True)
    article_link = models.TextField(blank=True, null=True)
    wikipedia = models.TextField(blank=True, null=True)
    video_link = models.TextField(blank=True, null=True)
    youtube_id = models.TextField(blank=True, null=True)
    flickr_images = models.ManyToManyField(FlickrImages, blank=True)

    def __str__(self):
        return self.mission_patch + ' ' + self.mission_patch_small
