from django .urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path( 'post/<int:post_id>', views.post, name= 'post'),
    path( 'sobre/', views.sobre, name= 'sobre'),
    path( 'contato/', views.contato, name= 'contato'),
    path( 'mensagens/', views.mensagens, name= 'mensagens'),
    path( 'mensagens/', views.cadastro, name= 'cadastro'),
    path( 'mensagens/<int:mensagens_id>/editar', 
         views.editar_mensagens, 
         name= 'editar_mensagens')
    ]
path('mensagens/<int:mensagem_id>/deletar/',
         views.deletar_mensagem,
         name='deletar_mensagem'
        ),