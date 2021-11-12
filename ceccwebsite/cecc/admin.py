from django.contrib import admin

from .models import Comment
from .models import Ceccmenu
from .models import CeccEvent

admin.site.register(Comment)
admin.site.register(Ceccmenu)
admin.site.register(CeccEvent)