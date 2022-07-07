import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    senha = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.nome_funcionario
class Usuario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome_usuario = models.CharField(max_length=200)
class RegistroPontos(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ponto_data = models.DateTimeField('Data do Ponto')
    def __str__(self) -> str:
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='ponto_data',
        description='Registro recene?',
    )
    def foi_registrado_recente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.ponto_data <= now
        #self.pub_date >= timezone.now() - datetime.timedelta(days=1)