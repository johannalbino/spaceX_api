from django.db import models
from first_stage.models import FirstStage
from second_stage.models import SecondStage
from fairings.models import Fairings

# Create your models here.


class Rocket(models.Model):
    rocket_id = models.CharField(max_length=50)
    rocket_name = models.CharField(max_length=50)
    rocket_type = models.CharField(max_length=30)
    first_stage = models.OneToOneField(FirstStage, on_delete=models.PROTECT)
    second_stage = models.OneToOneField(SecondStage, on_delete=models.PROTECT)
    fairings = models.OneToOneField(Fairings, on_delete=models.PROTECT)
