from django.urls import path
from django.urls import include
from session.views import salir

urlpatterns = [
    path('', salir, name='logout'), #cerrar sesion
]
