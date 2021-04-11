from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .forms import CreatePlaylistForm
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
    #Remover faixa da playlist
    if request.method == 'POST':
        data = request.POST.dict()
        idfaixa = int(data['id_faixa'])
        idplaylist = int(data['id_playlist'])
        requests.delete(f'{api_url}/faixaplaylist/{idplaylist}/{idfaixa}')
        return redirect(f'/playlistIndividual/{id}')

    return render(request, 'playlistInd.html', {"playInd": playInd, "faiPlay":faiPlay, "faiLista":faiLista})




def newPlaylist (request):
    if request.method == 'POST':
        form = CreatePlaylistForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            descricao = form.cleaned_data.get('descricao')
            criaPlaylist = requests.post(f'{api_url}/playlist',{'nome':nome,'descricao':descricao})
            return redirect('playlist')
    return render(request, 'newPlaylist.html', {})


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
    playAlb = requests.get(f'{api_url}/playlist')
    playAlb = playAlb.json()
    #Adicionar faixas a playlist
    if request.method == 'POST':
        data = request.POST.dict()
        idfaixa = int(data['id_faixa'])
        idplaylist = int(data['id_playlist'])
        requests.post(f'{api_url}/faixaplaylist/',{'id_faixa':idfaixa,'id_playlist':idplaylist})
    return render(request,'fullAlbum.html', {"fullAlb":fullAlb,"faiAlb":faiAlb,"playAlb":playAlb})

    
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

