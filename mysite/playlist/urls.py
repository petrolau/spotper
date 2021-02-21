from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('playlist',views.playlist, name = 'playlist'),
    path('newPlaylist',views.newPlaylist, name = 'newPlaylist'),
    path('albumList',views.albumList, name = 'albumList'),
    path('fullAlbum',views.fullAlbum, name = 'fullAlbum'),




]