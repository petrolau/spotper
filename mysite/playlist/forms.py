from django import forms

class CreatePlaylistForm(forms.Form):
    nome = forms.CharField(label='Nome playlist', max_length=30)
    descricao = forms.CharField(label='Descrição', max_length=50)