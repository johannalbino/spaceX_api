from django.contrib import admin
from .models import Launches, LaunchFailureDetails

# Register your models here.

admin.site.register(Launches)
admin.site.register(LaunchFailureDetails)