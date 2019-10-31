from django.db import models
from first_stage.models import FirstStage
from second_stage.models import SecondStage
from fairings.models import Fairings

# Create your models here.


class Rocket(models.Model):
    rocket_id = models.CharField(max_length=50, blank=True, null=True)
    rocket_name = models.CharField(max_length=50, blank=True, null=True)
    rocket_type = models.CharField(max_length=30, blank=True, null=True)
    first_stage = models.ForeignKey(FirstStage, on_delete=models.CASCADE, blank=True, null=True)
    second_stage = models.ForeignKey(SecondStage, on_delete=models.CASCADE, blank=True, null=True)
    fairings = models.ForeignKey(Fairings, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.rocket_id)
