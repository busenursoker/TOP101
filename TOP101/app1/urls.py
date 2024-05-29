from django.contrib import admin
from django.urls import path, include
from . import views
from .views import favorites_list, add_favorite, remove_favorite

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('movie', views.movie, name='movie'),
    path('movies', views.movies, name='movies'),
    path('register', views.register, name='register'),
    path('TVshows', views.TVshows, name='TVshows'),
    path('signout', views.signout, name="signout"),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites_list/', views.favorites_list, name='favorites_list'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:favorite_id>/', views.remove_favorite, name='remove_favorite'),
]