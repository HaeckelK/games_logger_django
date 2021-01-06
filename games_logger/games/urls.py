from django.urls import path
from games import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]