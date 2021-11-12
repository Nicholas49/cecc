from django.contrib import admin

from .models import jeopardyboard, CategoryTitle, finaljeopardy, team, wizard

admin.site.register(jeopardyboard)
admin.site.register(CategoryTitle)
admin.site.register(finaljeopardy)
admin.site.register(team)
admin.site.register(wizard)