
from django.contrib import admin
from django.urls import path
from core.views import * 

urlpatterns = [
    path('',index),
    path('index',index),
    path('admin/', admin.site.urls),
    
    #geral
    path('user_geral/lista_curso',lista_curso),
    path('user_geral/detalhe_cursotecnico', detalhe_cursotecnico),
    path('user_geral/detalhe_graduacao', detalhe_graduacao),
    path('user_geral/detalhe_posmba', detalhe_posmba),
    path('user_geral/disciplina', disciplina),
    path('user_geral/login', login),
    path('user_geral/noticias_faculdade', noticias_faculdade),
    path('user_geral/noticias_linguagens', noticias_linguagens),
    path('user_geral/noticias_tecnologia', noticias_tecnologia),
    
    # professor
    path('user_professor/area_professor', area_professor),
    path('user_professor/fechamento_nota', fechamento_nota),
    path('user_professor/smartclass', smartclass),
    path('user_professor/lancamento_nota', lancamento_nota),
    
    #aluno
    
    path('user_aluno/area_aluno', area_aluno),
    path('user_aluno/atividade', atividade),
    path('user_aluno/inscricao_curso', inscricao_curso),
    path('user_aluno/matricula_curso', matricula_curso),
    path('user_aluno/mensagem', mensagem),
    
    #coordenador
    path('user_coordenador/area_coordenador', area_coordenador),
    path('user_coordenador/cadastro_aluno_professor', cadastro_aluno_professor)

]
