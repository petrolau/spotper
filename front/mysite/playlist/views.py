from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
import requests

# Create your views here.

api_url = 'http://127.0.0.1:5000'
def home (request):
    return render(request, 'home.html', {})


def playlist (request):
    #response = requests.get(f'{api_url}/playlist')
    response = [
        {
            "id": 1,
            "nome": "playlist", 
            "musicas" : 5,
            "cria" : "hoje"
        },
        {
            "id": 2,
            "nome": "playlist", 
            "musicas" : 5,
            "cria" : "hoje"
        },
        {
            "id": 3,
            "nome": "playlist", 
            "musicas" : 5,
            "cria" : "hoje"
        },
    ]
    #response = response.json()
    return render(request, 'playlist.html', {"playlist":response})


#Tentar pegar a lista de albuns do banco de verdade
#response = requests.get(url)
#albuns = response.json() 
#return render(request, 'fullAlbum.html',{"response":response})

def playlistIndividual (request, id = 1):
    #details = requests.get(f'{api_url}/playlist/{id}')
    #songs = requests.get(f'{api_url}/playlist/{id}/songs')
    playInd = {
        "nome" : "eeeeeee",
        "descricao": "deu certo"
    }
    if id == 2:
        playInd = {
        "nome" : "asdasd",
        "descricao": "show"
    }
    return render(request, 'playlistInd.html', {"playInd": playInd})

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

