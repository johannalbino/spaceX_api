from django.db import models

# Create your models here.


class Telemetry(models.Model):
    flight_club = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.flight_club)