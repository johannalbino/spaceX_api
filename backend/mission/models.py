from django.db import models

# Create your models here.


class Mission(models.Model):
    mission_id = models.CharField(max_length=100)

    def __str__(self):
        return self.mission_id
