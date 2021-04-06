from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .forms import playForm
import requests

# Create your views here.

api_url = 'http://127.0.0.1:5000'
def home (request):
    return render(request, 'home.html', {})


def playlist (request):
    listaPlaylist =requests.get(f'{api_url}/playlist')
    listaPlaylist = listaPlaylist.json()
    return render(request, 'playlist.html', {"listaPlaylist":listaPlaylist})


def playlistIndividual (request, id = 1):
    playInd = requests.get(f'{api_url}/playlist/{id}')
    playInd = playInd.json()
    faiPlay = requests.get(f'{api_url}/faixaplaylist/{id}')
    faiPlay = faiPlay.json()
    faiLista = requests.get(f'{api_url}/faixa')
    faiLista = faiLista.json()
    addFaixa = requests.post(f'{api_url}/faixaplaylist/{id}')


    return render(request, 'playlistInd.html', {"playInd": playInd, "faiPlay":faiPlay, "faiLista":faiLista,"addFaixa":addFaixa})

##problema com form.
def newPlaylist (request):
    criaPlaylist = requests.post(f'{api_url}/playlist') 
    return render(request, 'newPlaylist.html', {"criaPlaylist":criaPlaylist})

def albumList (request):
    listagemAlbum = requests.get(f'{api_url}/album')
    gravadora = requests.get(f'{api_url}/gravadora')
    listagemAlbum = listagemAlbum.json()
    gravadora = gravadora.json()
    return render(request, 'albumList.html', {"listagemAlbum":listagemAlbum,"gravadora":gravadora})



def fullAlbum (request, id = 1):
    fullAlb = requests.get(f'{api_url}/album/{id}')
    fullAlb = fullAlb.json()
    faiAlb = requests.get(f'{api_url}/faixa/{id}')
    faiAlb = faiAlb.json()
    return render(request,'fullAlbum.html', {"fullAlb":fullAlb,"faiAlb":faiAlb})

    
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

