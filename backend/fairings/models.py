from django.db import models

# Create your models here.


class Fairings(models.Model):
    reused = models.BooleanField(blank=True, null=True)
    recovery_attempt = models.BooleanField(blank=True, null=True)
    recovered = models.BooleanField(blank=True, null=True)
    ship = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.reused)