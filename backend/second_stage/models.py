from django.db import models

# Create your models here.


class OrbitParams(models.Model):
    reference_system = models.CharField(max_length=50)
    regime = models.CharField(max_length=50)
    longitude = models.IntegerField()
    semi_major_axis_km = models.CharField(max_length=50, blank=True, null=True)
    eccentricity = models.CharField(max_length=50, blank=True, null=True)
    periapsis_km = models.CharField(max_length=50, blank=True, null=True)
    apoapsis_km = models.CharField(max_length=50, blank=True, null=True)
    inclination_deg = models.CharField(max_length=50, blank=True, null=True)
    period_min = models.CharField(max_length=50, blank=True, null=True)
    lifespan_years = models.IntegerField()
    epoch = models.CharField(max_length=50, blank=True, null=True)
    mean_motion = models.CharField(max_length=50, blank=True, null=True)
    raan = models.CharField(max_length=50, blank=True, null=True)
    arg_of_pericenter = models.CharField(max_length=50, blank=True, null=True)
    mean_anomaly = models.CharField(max_length=50, blank=True, null=True)


class Customers(models.Model):
    customers_name = models.CharField(max_length=50)


class Norad(models.Model):
    norad_name = models.CharField(max_length=50)


class Payloads(models.Model):
    payload_id = models.CharField(max_length=100)
    norad_id = models.ManyToManyField(Norad)
    reused = models.BooleanField()
    customers = models.ManyToManyField(Customers)
    nationality = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    payload_type = models.CharField(max_length=100)
    payload_mass_kg = models.IntegerField()
    payload_mass_lbs = models.DecimalField(max_digits=12, decimal_places=2)
    orbit = models.CharField(max_length=30)
    orbit_params = models.OneToOneField(OrbitParams, on_delete=models.PROTECT)
    uid = models.CharField(max_length=30)


class SecondStage(models.Model):
    block = models.IntegerField()
    payloads = models.OneToOneField(Payloads, on_delete=models.PROTECT)