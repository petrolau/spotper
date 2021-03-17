from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home (request):
    return render(request, 'home.html', {})

def playlist (request):
    return render(request, 'playlist.html', {})

def playlistIndividual (request):
    return render(request, 'playlistInd.html', {})

def newPlaylist (request):
    return render(request, 'newPlaylist.html', {})

def albumList (request):
    return render(request, 'albumList.html', {})

def fullAlbum (request):
    return render(request, 'fullAlbum.html', {})

    
def registro (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

