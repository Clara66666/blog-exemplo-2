from django import forms

class Mensagemform(forms.Form):
    nome_completo = forms.CharField(
        widget= forms.Textarea(attrs ={"class": "form-control"}),
        max_length=100,
        label="Digite seu nome"
    )


    email = forms.EmailField(
    widget= forms.Textarea(attrs ={"class": "form-control"}),
    label="Digite seu email"
    )

    telefone = forms.CharField(
        max_length=12,
        widget= forms.Textarea(attrs ={"class": "form-control"}),
        label="Digite seu telefone"
    )
    
   
    cidade = forms.CharField(
        widget= forms.Textarea(attrs ={"class": "form-control"}),
        max_length=100,
        required=False,
    )
    
    mensagem = forms.CharField(
        max_length=1000,
        widget= forms.Textarea(attrs ={"class": "form-control"}),
        label="Digite sua mensagem"
    )
