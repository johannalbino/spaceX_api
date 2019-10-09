from django.db import models

# Create your models here.


class Ships(models.Model):
    ships_name = models.CharField(max_length=100)