from django.urls import path
from django.urls import include
from operations.views import BasculaView, ClienteView, CrearClienteView


urlpatterns = [
    path('entradas-operations/', BasculaView.as_view(), name='dashboard_operations'),
    path('clientes-operations/', ClienteView.as_view(), name='clientes_operations'),
    path('crear-cliente/', CrearClienteView.as_view(), name='crear_cliente'),
]