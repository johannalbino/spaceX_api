from django.db import models

# Create your models here.


class Cores(models.Model):
    core_serial = models.CharField(max_length=100)
    flight = models.IntegerField()
    block = models.IntegerField()
    gridfins = models.BooleanField()
    legs = models.BooleanField()
    reused = models.BooleanField()
    land_success = models.CharField(max_length=100, blank=True, null=True)
    landing_intent = models.BooleanField()
    landing_type = models.CharField(max_length=100, blank=True, null=True)
    landing_vehicle = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.core_serial + ' ' + str(self.flight)


class FirstStage(models.Model):
    cores = models.ManyToManyField(Cores)

    def __str__(self):
        return str(self.cores)