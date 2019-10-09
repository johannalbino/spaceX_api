from django.contrib import admin
from .models import Links
from .models import FlickrImages

# Register your models here.

admin.site.register(Links)
admin.site.register(FlickrImages)