from django.shortcuts import render
from django.views.generic import TemplateView,ListView

# Create your views here.

class Index(TemplateView):
    template_name = "home/index.html"

class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['Harry Potter y la Piedra Filosofal','La larga marcha','Inferno','Juego de tronos','El hobbit']
    context_object_name = "libros"