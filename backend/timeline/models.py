from django.db import models

# Create your models here.


class Timeline(models.Model):
    webcast_liftoff = models.IntegerField()
    go_for_prop_loading = models.IntegerField()
    rp1_loading = models.IntegerField()
    stage1_lox_loading = models.IntegerField()
    stage2_lox_loading = models.IntegerField()
    engine_chill = models.IntegerField()
    prelaunch_checks = models.IntegerField()
    propellant_pressurization = models.IntegerField()
    go_for_launch = models.IntegerField()
    ignition = models.IntegerField()
    liftoff = models.IntegerField()
    maxq = models.IntegerField()
    meco = models.IntegerField()
    stage_sep = models.IntegerField()
    second_stage_ignition = models.IntegerField()
    seco1 = models.IntegerField()
    dragon_separation = models.IntegerField()
    dragon_solar_deploy = models.IntegerField()
    dragon_bay_door_deploy = models.IntegerField()

    def __str__(self):
        return str(self.webcast_liftoff)