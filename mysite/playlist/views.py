from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'home.html', {})

def playlist (request):
    return render(request, 'playlist.html', {})

def newPlaylist (request):
    return render(request, 'newPlaylist.html', {})

def albumList (request):
    return render(request, 'albumList.html', {})

def fullAlbum (request):
    return render(request, 'fullAlbum.html', {})