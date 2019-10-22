from django.db import models

# Create your models here.


class Ships(models.Model):
    ships = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.ships)