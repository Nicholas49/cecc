from django.urls import path

from . import views

urlpatterns = [
    path('<str:version>/front/', views.front, name='front'),
    path('<str:version>/create_user/', views.create_user, name='create_user'),
    path('<str:version>/submitballot/', views.submitballot, name='submitballot'),
    path('<str:version>/chart/', views.chart, name='chart'),
    path('<str:version>/passpage/', views.passpage, name='passpage'),
    path('<str:version>/passpage/<str:error>', views.passpage, name='passpage'),
    path('<str:version>/passpage/<str:error>/<str:code>', views.passpage, name='passpage'),
    path('<str:version>/loadballot/', views.loadballot, name='loadballot'),
    path('<str:version>/loadballot/<str:code>', views.loadballot, name='loadballot'),
    path('<str:version>/logout_user', views.logout_user, name='logout_user'),
    path('<str:version>/login_user', views.login_user, name='login_user'),
    path('showhash/<str:text>', views.showhash, name='showhash'),
    path('winnerform', views.winnerform, name='winnerform'),
    path('submit_winners', views.submit_winners, name='submit_winners')
]
