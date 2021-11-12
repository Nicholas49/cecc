from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('play', views.board, name='board'),
    path('play/<str:game_name>', views.board, name='board'),
    path('double/<str:game_name>', views.board2, name='board2'),
    path('showanswer1/<str:game_name>/<str:jcat>/<str:dollar>', views.showanswer1, name='showanswer1'),
    path('showanswer2/<str:game_name>/<str:jcat>/<str:dollar>/<int:turn>', views.showanswer2, name='showanswer2'),
    path('showexample/<str:game_name>/<str:jcat>', views.showexample, name='showexample'),
    path('reset/<str:gname>', views.reset, name='reset'),
    path('final/<str:game_name>', views.final, name='final'),
    path('create_game', views.edit_game, name='edit_game'),
    path('make_game', views.make_game, name='make_game'),
    path('make_category', views.make_category, name='make_category'),
    path('make_final', views.make_final, name='make_final'),
    path('create_game/<str:game_name>', views.edit_game, name='edit_game'),
    path('create_game2/<str:game_name>', views.edit_game2, name='edit_game2'),
    path('create_gamef/<str:game_name>', views.edit_gamef, name='edit_gamef'),
    path('tallypoints', views.tallypoints, name='tallypoints'),
    path('tallydouble', views.tallydouble, name='tallydouble'),
    path('endgame', views.endgame, name='endgame'),
    path('results/<int:topscore>/<str:winner>/<str:game_name>', views.results, name='results'),
    path('editteam', views.editteam, name='editteam'),
    path('delete_game/<str:game_name>', views.delete_game, name='delete_game'),
    path('change_name', views.change_name, name='change_name'),
    path('move_turn', views.move_turn, name='move_turn'),
    path('shiftup', views.shiftup, name='shiftup'),
    path('shiftdown', views.shiftdown, name='shiftdown'),
    path('shiftright', views.shiftright, name='shiftright'),
    path('hello', views.hello, name='hello')
]
