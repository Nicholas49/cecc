from django.contrib import admin

from .models import oscarballot
from .models import umslballot
from .models import Winners

admin.site.register(oscarballot)
admin.site.register(umslballot)
admin.site.register(Winners)