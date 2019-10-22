from django.db import models
from mission.models import Mission
from rocket.models import Rocket
from ships.models import Ships
from telemetry.models import Telemetry
from launch_site.models import LaunchSite
from links.models import Links
from timeline.models import Timeline


class History(models.Model):
    first_time = models.BooleanField(default=True)
    latest_launche = models.IntegerField(null=True, blank=True)
    next_launche = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.first_time)


class LaunchFailureDetails(models.Model):
    time = models.IntegerField(blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.time)


class Launches(models.Model):
    flight_number = models.IntegerField(blank=True, null=True)
    mission_name = models.CharField(max_length=100, blank=True, null=True)
    mission_id = models.ManyToManyField(Mission, blank=True)
    launch_year = models.IntegerField(blank=True, null=True)
    launch_date_unix = models.IntegerField(blank=True, null=True)
    launch_date_utc = models.DateTimeField(blank=True, null=True)
    launch_date_local = models.DateTimeField(blank=True, null=True)
    is_tentative = models.BooleanField(blank=True, null=True)
    tentative_max_precision = models.CharField(max_length=30, blank=True, null=True)
    tbd = models.BooleanField(blank=True, null=True)
    launch_window = models.IntegerField(blank=True, null=True)
    rocket = models.ForeignKey(Rocket, on_delete=models.PROTECT, blank=True, null=True)
    ships = models.ManyToManyField(Ships, blank=True)
    telemetry = models.ForeignKey(Telemetry, on_delete=models.CASCADE, blank=True, null=True)
    launch_site = models.ForeignKey(LaunchSite, on_delete=models.CASCADE, blank=True, null=True)
    launch_success = models.BooleanField(blank=True, null=True)
    launch_failure_details = models.ForeignKey(LaunchFailureDetails, on_delete=models.CASCADE, blank=True, null=True)
    links = models.ForeignKey(Links, on_delete=models.PROTECT, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    upcoming = models.BooleanField(blank=True, null=True)
    static_fire_date_utc = models.DateTimeField(blank=True, null=True)
    static_fire_date_unix = models.IntegerField(blank=True, null=True)
    timeline = models.ForeignKey(Timeline, on_delete=models.PROTECT, blank=True, null=True)
    crew = models.CharField(max_length=50, blank=True, null=True)
    last_date_update = models.DateTimeField(blank=True, null=True)
    last_ll_launch_date = models.DateTimeField(blank=True, null=True)
    last_ll_update = models.DateTimeField(blank=True, null=True)
    last_wiki_launch_date = models.DateTimeField(blank=True, null=True)
    last_wiki_revision = models.CharField(max_length=100, null=True, blank=True)
    last_wiki_update = models.DateTimeField(blank=True, null=True)
    launch_date_source = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.flight_number)

