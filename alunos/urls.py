from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.novo_aluno, name='novo_aluno'),
    path('editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('detalhes/<int:id>/', views.detalhes_aluno, name='detalhes_aluno'),
    path('remover/<int:id>/', views.remover_aluno, name='remover_aluno'),
]
