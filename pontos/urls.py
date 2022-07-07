from django.urls import URLPattern, path

from . import views

URLPattern = [
    path("",  views.IndexView.as_view() , name='index'),
]