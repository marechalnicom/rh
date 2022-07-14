from django.urls import  path

from . import views

app_name ='pontos'
urlpatterns = [
    path("",  views.IndexView.as_view() , name='index'),
    path("registros", views.registro, name="registros"),
    path("empresas", views.empresa, name="empresas"),
]