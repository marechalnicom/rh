from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import *

class IndexView(generic.ListView):
    template_name = 'pontos/index.html'
    context_object_name = 'lista_empresas'

    def get_queryset(self):
        return Empresa.objects.all()
class RegistrosView(generic.ListView):
    template_name = 'pontos/registros.html'
    context_object_name = 'lista_ultimos_pontos'

    def get_queryset(self):
        return RegistroPontos.objects.filter(
            ponto_data__lte=timezone.now()
        ).order_by('-ponto_data')[:5]