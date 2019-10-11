from django.db import models

# Create your models here.


class Ships(models.Model):
    ships = models.CharField(max_length=100)

    def __str__(self):
        return self.ships