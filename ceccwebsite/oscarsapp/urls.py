from django.urls import path

from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('create_user/', views.create_user, name='create_user'),
    path('submitballot/', views.submitballot, name='submitballot'),
    path('chart/', views.chart, name='chart'),
    path('passpage/', views.passpage, name='passpage'),
    path('passpage/<str:error>', views.passpage, name='passpage'),
    path('loadballot/', views.loadballot, name='loadballot'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('login_user', views.login_user, name='login_user'),
    path('umsl/', views.ufront, name='ufront'),
    path('umsl/create_user/', views.ucreate_user, name='ucreate_user'),
    path('umsl/submitballot/', views.usubmitballot, name='usubmitballot'),
    path('umsl/chart/', views.uchart, name='uchart'),
    path('umsl/passpage/', views.upasspage, name='upasspage'),
    path('umsl/passpage/<str:error>', views.upasspage, name='upasspage'),
    path('umsl/loadballot/', views.uloadballot, name='uloadballot'),
    path('umsl/logout_user', views.ulogout_user, name='ulogout_user'),
    path('umsl/login_user', views.ulogin_user, name='ulogin_user')
]
