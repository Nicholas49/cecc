from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('answerform', views.answerform, name='answerform'),
    path('answerform/<int:roundnum>', views.answerform, name='answerform'),
    path('maketeam', views.maketeam, name='maketeam'),
    path('loginteam', views.loginteam, name='loginteam'),
    path('submitanswers', views.submitanswers, name='submitanswers'),
    path('showanswers/', views.showanswers, name='showanswers'),
    path('showanswers/<int:roundnum>', views.showanswers, name='showanswers'),
    path('tallypoints', views.tallypoints, name='tallypoints'),
    path('logoutteam', views.logoutteam, name='logoutteam'),
    path('resetgame', views.resetgame, name='resetgame'),
    path('second', views.second, name='second')
]
