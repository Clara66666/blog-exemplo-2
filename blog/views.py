from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from .models import Post, Blog, Mensagem 
from .forms import Mensagemform


def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog" : Blog.objects.first()
    }
    return render(request, 'index.html', context)

def post(request, post_id ):
  
  context = {
         "posts": Post.objects.get(pk=post_id),
         "blog": Blog.objects.first()
    }
  return render(request,'post.html', context)


def sobre(request):
    context = {
         "blog": Blog.objects.first(),
}
    return render(request, 'sobre.html', context)


def contato(request):
   context = {
         "blog": Blog.objects.first(),
     
        
           }


   if  request.method == "POST":
      print(request.POST['nome'])
      print(request.POST['email'])
      print(request.POST['telefone'])
      print(request.POST['mensagem'])
      print(request.POST['cidade'])

      
    
   if request.method == "POST":
    form = Mensagemform(request.POST)
    if form.is_valid():
          mensagem.nome = form.cleaned_data['nome']
          mensagem.email = form.cleaned_data['email']
          mensagem.telefone = form.cleaned_data['telefone']
          mensagem = form.cleaned_data['mensagem']
          mensagem.cidade = form.cleaned_data['cidade']
          mensagem.save()
    return redirect(mensagem) 
   return render(request, "contact.html", context)

def mensagens(request):
   context = {
         "blog": Blog.objects.first(),

}
   return render(request, 'mensagens.html', context) 


def editar_mensagens(request, mensagem_id):
   mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
   context = {
      "blog": Blog.objects.first(),
      "form": Mensagemform(initial=model_to_dict(mensagem))
   }

   return render(request, 'mensagens.html', context) 


def deletar_mensagem(request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem": get_object_or_404(Mensagem, pk=mensagem_id)
    }

    if request.method=="POST":
        context["mensagem"].delete()
        return redirect('mensagens')
    else:
        return render(request, "delete_contact.html", context)
                                                                                             