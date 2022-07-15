from django.urls import  path

from . import views

app_name ='pontos'
urlpatterns = [
    path("",  views.IndexView.as_view() , name='index'),
    path("pontos", views.PontoView.as_view(), name="pontos"),
    path("empresas", views.empresa, name="empresas"),
    path("funcionarios", views.funcionario, name="funcionarios"),
    path("registros", views.registro, name="registros"),
]