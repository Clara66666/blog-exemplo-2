from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
  class Meta:
    model = Mensagem
    fields = [ 'nome', 'email','telefone','cidade','mensagem']


  def clean_estado(self):
    data = self.cleaned_data["estado"]
    estados_validos = ['bom jesus', 'spp', 'joao pessoa']
    if (not data in estados_validos):
        raise("a cidade informada não é permitida!") 

    return data 

