from django import forms

class playForm(forms.Form):
    nome = forms.CharField(label='Nome da playlist', max_length=30)
    descricao = forms.CharField(label = 'Descrição', max_length=50)