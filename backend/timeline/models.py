from django.db import models

# Create your models here.


class Timeline(models.Model):
    webcast_liftoff = models.IntegerField(blank=True, null=True)
    go_for_prop_loading = models.IntegerField(blank=True, null=True)
    rp1_loading = models.IntegerField(blank=True, null=True)
    stage1_lox_loading = models.IntegerField(blank=True, null=True)
    stage2_lox_loading = models.IntegerField(blank=True, null=True)
    engine_chill = models.IntegerField(blank=True, null=True)
    prelaunch_checks = models.IntegerField(blank=True, null=True)
    propellant_pressurization = models.IntegerField(blank=True, null=True)
    go_for_launch = models.IntegerField(blank=True, null=True)
    ignition = models.IntegerField(blank=True, null=True)
    liftoff = models.IntegerField(blank=True, null=True)
    maxq = models.IntegerField(blank=True, null=True)
    meco = models.IntegerField(blank=True, null=True)
    stage_sep = models.IntegerField(blank=True, null=True)
    second_stage_ignition = models.IntegerField(blank=True, null=True)
    seco1 = models.IntegerField(blank=True, null=True)
    dragon_separation = models.IntegerField(blank=True, null=True)
    dragon_solar_deploy = models.IntegerField(blank=True, null=True)
    dragon_bay_door_deploy = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.webcast_liftoff)