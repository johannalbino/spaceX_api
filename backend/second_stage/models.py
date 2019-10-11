from django.db import models

# Create your models here.


class OrbitParams(models.Model):
    reference_system = models.CharField(max_length=50)
    regime = models.CharField(max_length=50)
    longitude = models.IntegerField(blank=True, null=True)
    semi_major_axis_km = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    eccentricity = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    periapsis_km = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    apoapsis_km = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    inclination_deg = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    period_min = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    lifespan_years = models.IntegerField(blank=True, null=True)
    epoch = models.CharField(max_length=50, blank=True, null=True)
    mean_motion = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    raan = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    arg_of_pericenter = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    mean_anomaly = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    def __str__(self):
        return self.reference_system + ' ' + self.regime


class Customers(models.Model):
    customers = models.CharField(max_length=50)

    def __str__(self):
        return self.customers


class Norad(models.Model):
    norad_id = models.CharField(max_length=50)

    def __str__(self):
        return self.norad_id


class Payloads(models.Model):
    payload_id = models.CharField(max_length=100)
    norad_id = models.ManyToManyField(Norad, blank=True)
    cap_serial = models.CharField(max_length=50, blank=True, null=True)
    reused = models.BooleanField()
    customers = models.ManyToManyField(Customers, blank=True)
    nationality = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    payload_type = models.CharField(max_length=100)
    payload_mass_kg = models.IntegerField()
    payload_mass_lbs = models.DecimalField(max_digits=12, decimal_places=2)
    orbit = models.CharField(max_length=30)
    orbit_params = models.ForeignKey(OrbitParams, on_delete=models.PROTECT, blank=True, null=True)
    mass_returned_kg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    mass_returned_lbs = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    flight_time_sec = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cargo_manifest = models.CharField(max_length=30, blank=True, null=True)
    uid = models.CharField(max_length=30)

    def __str__(self):
        return self.payload_id


class SecondStage(models.Model):
    block = models.IntegerField()
    payloads = models.ManyToManyField(Payloads)