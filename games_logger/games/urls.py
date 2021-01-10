from django.urls import path
from games import views

urlpatterns = [
    path('', views.index, name='index'),
    path("player/<int:pk>/", views.player_detail, name="player"),
    path("players/", views.players, name="players"),
    path("gallery/", views.gallery, name="gallery"),
    path("game/<int:pk>/", views.game_detail, name="game_detail"),
    path("random_game/", views.random_game, name="random_game"),
    path("matches/", views.matches, name="matches"),
]