from django.contrib import admin
from .models import Launches, LaunchFailureDetails, History

# Register your models here.

admin.site.register(Launches)
admin.site.register(LaunchFailureDetails)
admin.site.register(History)