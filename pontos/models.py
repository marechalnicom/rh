import datetime
from operator import mod

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Empresa(models.Model):
    nome_empresa = models.CharField('Nome da Empresa', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=20, blank=True) # cnpj usa 18 com 14 nueros e 4 simbolos
    ie = models.CharField('IE', max_length=10, blank=True) # ie usa 9
    '''A Inscrição Estadual é um número composto por nove dígitos.
        Independentemente do Estado, a IE sempre terá nove dígitos que significam:

        Os 2 primeiros números indicam o estado de cadastro;
        Os 6 números são os números de inscrição de cada empresa
        O último dígito é o verificador ou dígito de controle. '''
    def __str__(self) -> str:
        return self.nome_empresa
class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome_funcionario = models.CharField('Nome do Funcionário', max_length=100)
    horario = models.CharField('Horário',max_length=200)
    senha = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.nome_funcionario
class Usuario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome_usuario = models.CharField('Usuário', max_length=100)
    def __str__(self) -> str:
        return self.nome_usuario
class RegistroPontos(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ponto_data = models.DateTimeField('Data do Ponto',default=timezone.now())
    ativo = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.ponto_data
    @admin.display(
        boolean=True,
        ordering='ponto_data',
        description='Registro recente?',
    )
    def foi_registrado_recente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.ponto_data <= now
        #self.pub_date >= timezone.now() - datetime.timedelta(days=1)