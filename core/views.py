from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

#Geral

def lista_curso(request):
    return render(request, "user_geral/lista_curso.html")

def detalhe_cursotecnico(request):
    return render(request, "user_geral/detalhe_cursotecnico.html")

def detalhe_graduacao(request):
    return render(request, "user_geral/detalhe_graduacao.html")

def detalhe_posmba(request):
    return render(request, "user_geral/lisdetalhe_posmba.html")

def disciplina(request):
    return render(request, "user_geral/disciplina.html")

def login(request):
    return render(request, "user_geral/login.html")

def noticias_faculdade(request):
    return render(request, "user_geral/noticias_faculdade.html")

def noticias_linguagens(request):
    return render(request, "user_geral/noticias_linguagens.html")

def noticias_tecnologia(request):
    return render(request, "user_geral/noticias_tecnologia.html")

#professor
def area_professor(request):
    return render(request, "user_professor/area_professor.html")

def fechamento_nota(request):
    return render(request, "user_professor/fechamento_nota.html")

def lancamento_nota(request):
    return render(request, "user_professor/lancamento_nota.html")

def smartclass(request):
    return render(request, "user_professor/smartclass.html")

#coordenador
def cadastro_aluno_professor(request):
    return render(request, "user_coordenador/cadastro_aluno_professor.html")

def area_coordenador(request):
    return render(request, "user_coordenador/area_coordenador.html")
#aluno
def area_aluno(request):
    return render(request, "user_aluno/area_aluno.html")

def atividade(request):
    return render(request, "user_aluno/atividade.html")

def inscricao_curso(request):
    return render(request, "user_aluno/inscricao_curso.html")

def matricula_curso(request):
    return render(request, "user_aluno/matricula_curso.html")

def mensagem(request):
    return render(request, "user_aluno/mensagem.html")






