from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign, name='sign'),
    path('passwordpage/', views.passwordpage, name='passwordpage'),
    path('delmenu/', views.delmenu, name='delmenu'),
    path('addmenu/', views.addmenu, name='addmenu'),
    path('addevent/', views.addevent, name='addevent'),
    path('history/', views.history, name='history'),
    path('programs/', views.programs, name='programs'),
    path('photos/', views.photos, name='photos'),
    path('video/', views.video, name='video'),
    path('schedules/', views.schedules, name='schedules'),
    path('mrdcnewsletter/', views.mrdcnewsletter, name='mrdcnewsletter'),
    path('ceccnewsletter/', views.ceccnewsletter, name='ceccnewsletter'),
    path('mrdcmenus/', views.mrdcmenus, name='mrdcmenus'),
    path('ceccmenus/', views.ceccmenus, name='ceccmenus'),
    path('contact/', views.contact, name='contact')
]
