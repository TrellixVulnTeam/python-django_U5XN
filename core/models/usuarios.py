from django.db import models
from datatime  import date


class Usuario(models.Model):
    nome            =           models.TextField(max_length=255)
    email           =           models.TextField(max_length=255)
    celular         =           models.TextField(max_length=20)
    dt_expericao    =           models.DateField(default = date(year=1900, month=1, day=1))#Confirmar
    login           =           models.TextField(max_length=20,unique=True)
    senha           =           models.TextField(max_length=20)



class Coordenador(Usuario):
    pass


class Aluno(Usuario):
    ra      =       models.IntegerField()
    foto    =       models.TextField(max_length=255)



class Professor():
    apelido     =       models.TextField(max_length=255)



