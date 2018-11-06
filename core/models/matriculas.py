from  django.db import models
from .usuarios import Aluno, Coordenador
from .disciplinas import DisciplinaOfertada

class SolicitacaoMatricula(models.Model):
    dt_solicitacao          =           models.DateField()
    status                  =           models.TextField(max_length=255)
    aluno                   =           models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina_ofertada     =           models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    coordenador             =           models.ForeignKey(Coordenador, on_delete =models.PROTECT)


