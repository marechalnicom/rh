from django.contrib import admin

from .models import RegistroPontos, Usuario, Funcionario, Empresa

admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(RegistroPontos)
admin.site.register(Usuario)