from django.contrib import admin
from django.urls import path, include 
from playlist import views

urlpatterns = [
    #Admin area
    path('admin/', admin.site.urls),
    #Homepage
    path('', include('playlist.urls')),
]
