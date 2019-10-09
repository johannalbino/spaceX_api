from django.contrib import admin
from .models import SecondStage
from .models import OrbitParams
from .models import Customers
from .models import Norad
from .models import Payloads

# Register your models here.

admin.site.register(SecondStage)
admin.site.register(OrbitParams)
admin.site.register(Customers)
admin.site.register(Norad)
admin.site.register(Payloads)
