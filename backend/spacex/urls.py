"""spacex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import LaunchesViewSet
from mission.views import MissionViewSet
from rocket.views import RocketViewSet
from ships.views import ShipsViewSet
from telemetry.views import TelemetryViewSet
from launch_site.views import LaunchSiteViewSet
from links.views import LinksViewSet
from timeline.views import TimelineViewSet

router = routers.DefaultRouter()
router.register(r'launches', LaunchesViewSet)
#router.register(r'mission', MissionViewSet)
#router.register(r'rocket', RocketViewSet)
#router.register(r'ships', ShipsViewSet)
#router.register(r'telemetry', TelemetryViewSet)
#router.register(r'launch_site', LaunchSiteViewSet)
#router.register(r'links', LinksViewSet)
#router.register(r'timeline', TimelineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
