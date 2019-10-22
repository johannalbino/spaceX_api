from django.db import models

# Create your models here.


class LaunchSite(models.Model):
    site_id = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    site_name_long = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.site_id)