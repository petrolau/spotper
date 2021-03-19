from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name = 'home'),
    path('playlist',views.playlist, name = 'playlist'),
    path('playlistIndividual/<int:id>/',views.playlistIndividual, name = 'playlistIndividual'),
    path('newPlaylist',views.newPlaylist, name = 'newPlaylist'),
    path('albumList',views.albumList, name = 'albumList'),
    path('fullAlbum',views.fullAlbum, name = 'fullAlbum'),
    path('registro',views.registro, name = 'registro'),
    url(r'^registro/$', views.registro, name='registro'),

]