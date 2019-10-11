from django.db import models

# Create your models here.


class Cores(models.Model):
    core_serial = models.CharField(max_length=100, blank=True, null=True)
    flight = models.IntegerField(blank=True, null=True)
    block = models.IntegerField(blank=True, null=True)
    gridfins = models.BooleanField(blank=True, null=True)
    legs = models.BooleanField(blank=True, null=True)
    reused = models.BooleanField(blank=True, null=True)
    land_success = models.CharField(max_length=100, blank=True, null=True)
    landing_intent = models.BooleanField(blank=True, null=True)
    landing_type = models.CharField(max_length=100, blank=True, null=True)
    landing_vehicle = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.core_serial + ' ' + str(self.flight)


class FirstStage(models.Model):
    cores = models.ManyToManyField(Cores, blank=True)
