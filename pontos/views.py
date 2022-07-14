from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Empresa, Funcionario, Usuario, RegistroPontos

class IndexView(generic.ListView):
    template_name = 'pontos/index.html'
    context_object_name = 'lista_empresas'

    def get_queryset(self):
        return Empresa.objects.all()
#class RegistrosView(generic.ListView):
#    context_object_name = 'lista_ultimos_pontos'
#
    #def get_queryset(self):
    #    return RegistroPontos.objects.filter(
    #        ponto_data__lte=timezone.now()
    #    ).order_by('-ponto_data')[:5]
def empresa(request):
    empresas = Empresa.objects.all()
    resposta = {}
    #resposta = dict(empresas)
    for empresa in empresas:
        resposta[empresa.nome_empresa] = empresa.cnpj
    print (resposta,type(resposta))
    return JsonResponse(resposta)

def registro(request):
    registros = RegistroPontos.objects.filter(ponto_data__lte=timezone.now()).order_by('-ponto_data')[:15]
    resposta = {}
    for regis in registros:
        resposta[str(regis.ponto_data)] = str(regis.funcionario)
    print (resposta,type(resposta))

    return JsonResponse(resposta)