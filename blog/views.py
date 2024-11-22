from django.shortcuts import render
from .models import Post, Blog, Mensagem

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

      
      context['erro'] = []
      if not request.POST['nome']:
        context['erro']['nome'] = True
      if not request.POST['email']:
        context['erro']['email'] = True
      if not request.POST['telefone']:
        context['erro']['telefone'] = True
      if not request.POST['mensagem']:
        context['erro']['mensagem'] = True
      if  context["erro"]:
        return render(request, "edit_contato.html" , context)

      mensagem = context["mensagem"]
      mensagem.nome = request.POST['nome']
      mensagem.email = request.POST['email']
      mensagem.telefone = request.POST['telefone']
      mensagem.cidade = request.POST['cidade']
      mensagem.mensagem = request.POST['mensagem']                                     

   
      mensagem.save()

      return render(request, 'contato.html', context) 

   else: 
      return render(request, 'contato.html', context)
   
def mensagens(request):
   context = {
         "blog": Blog.objects.first(),

}
   return render(request, 'mensagens.html', context) 


def editar_mensagens(request):
   context = {
      "blog": Blog.objects.first(),
      "mensagens" : Mensagem.objects.get(pk=mensagens_id)
   }

   return render(request, 'mensagens.html', context) 


  if request.method=="POST":
     context["mensagem"].delete()
     return redirect('mensagem')
 else:
   return render(request, "delete_contato.html", context)


                                                                                             