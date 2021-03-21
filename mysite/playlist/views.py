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
        "descricao": "deu certo",
        "quant" : "300 musicas, 3h20min"
    }
    if id == 2:
        playInd = {
        "nome" : "asdasd",
        "descricao": "show",
        "quant" : "250 musicas, 2h40min"

    }
    return render(request, 'playlistInd.html', {"playInd": playInd})

def newPlaylist (request):
    return render(request, 'newPlaylist.html', {})

def albumList (request):
    listagemAlbum = [
        {
            "id": 1,
            "nome": "album1", 
            "gravadora" : "nome_gravadora",
            "datagravacao" : "15/02/2020",
            "precocompra" : "R$2500,00",
            "datacompra" : "24/07/1971",
            "tipocompra" : "virtual"

        },
       
    ]
    return render(request, 'albumList.html', {"listagemAlbum":listagemAlbum})



def fullAlbum (request, id = 1):
    fullAlb = {
        "nome" : "eeeeeee",
        "duracao": "3h20min"
    }
    if id == 2:
        fullAlb = {
        "nome" : "uhul",
        "duracao": "3h"

    }
    return render(request, 'fullAlbum.html', {"fullAlb":fullAlb})

    
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

