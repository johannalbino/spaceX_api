from django.db import models

# Create your models here.


class Fairings(models.Model):
    reused = models.BooleanField()
    recovery_attempt = models.BooleanField()
    recovered = models.BooleanField()
    ship = models.CharField(max_length=50)

    def __str__(self):
        return str(self.reused)
