from django.db import models

# Create your models here.


class LaunchSite(models.Model):
    site_id = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100)
    site_name_long = models.CharField(max_length=100)

    def __str__(self):
        return self.site_id + ' ' + self.site_name