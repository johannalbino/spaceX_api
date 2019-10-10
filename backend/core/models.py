from django.db import models
from mission.models import Mission
from rocket.models import Rocket
from ships.models import Ships
from telemetry.models import Telemetry
from launch_site.models import LaunchSite
from links.models import Links
from timeline.models import Timeline


# Create your models here.


class Launches(models.Model):
    flight_number = models.IntegerField()
    mission_name = models.CharField(max_length=100)
    mission_id = models.ManyToManyField(Mission)
    launch_year = models.IntegerField()
    launch_date_unix = models.IntegerField()
    launch_date_utc = models.DateTimeField(auto_now_add=False)
    launch_date_local = models.DateTimeField(auto_now_add=False)
    is_tentative = models.BooleanField(blank=True, null=True)
    tentative_max_precision = models.CharField(max_length=30, blank=True, null=True)
    tbd = models.BooleanField(blank=True, null=True)
    launch_window = models.IntegerField(blank=True, null=True)
    rocket = models.OneToOneField(Rocket, on_delete=models.PROTECT)
    ships = models.ManyToManyField(Ships, blank=True)
    telemetry = models.OneToOneField(Telemetry, on_delete=models.CASCADE)
    launch_site = models.OneToOneField(LaunchSite, on_delete=models.PROTECT)
    launch_success = models.BooleanField()
    links = models.OneToOneField(Links, on_delete=models.PROTECT)
    details = models.TextField(blank=True, null=True)
    upcoming = models.BooleanField()
    static_fire_date_utc = models.DateTimeField(auto_now_add=False)
    static_fire_date_unix = models.IntegerField()
    timeline = models.OneToOneField(Timeline, on_delete=models.CASCADE)
    crew = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.flight_number) + ' ' + self.mission_name

