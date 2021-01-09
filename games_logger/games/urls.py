from django.urls import path
from games import views

urlpatterns = [
    path('', views.index, name='index'),
    path("player/<int:pk>/", views.player_detail, name="player"),
    path("players/", views.players, name="players"),
]