from django.contrib import admin

from .models import Wizard, Ballot, Category, Nominee, Nomination, Pick

admin.site.register(Wizard)
admin.site.register(Ballot)
admin.site.register(Category)
admin.site.register(Nominee)
admin.site.register(Nomination)
admin.site.register(Pick)