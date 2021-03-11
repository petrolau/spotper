from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name = 'home'),
    path('playlist',views.playlist, name = 'playlist'),
    path ('playlistIndividual',views.playlistIndividual, name = 'playlistIndividual'),
    path('newPlaylist',views.newPlaylist, name = 'newPlaylist'),
    path('albumList',views.albumList, name = 'albumList'),
    path('fullAlbum',views.fullAlbum, name = 'fullAlbum'),

]