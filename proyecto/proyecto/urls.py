from django.contrib import admin
from django.urls import path
#Se debe importar la ruta de la vista
from PaginaWeb.views import PaginaPrincipal,nombreVista,noticias

#Se debe agregar la ruta en la que se mostrará la vista
urlpatterns = [
    path('NombreRuta/', nombreVista),
    path('PaginaPrincipal', PaginaPrincipal),path('noticias',noticias)
]
