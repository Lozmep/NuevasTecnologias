from django.contrib import admin
from django.urls import path
#Se debe importar la ruta de la vista
from PaginaWeb.views import PaginaPrincipal,nombreVista,noticias

#Se debe agregar la ruta en la que se mostrará la vista
urlpatterns = [

    path('', PaginaPrincipal),path('noticias',noticias),path('inicio', PaginaPrincipal)
]
