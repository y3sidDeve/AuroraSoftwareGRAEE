from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from session.mixins import TecnicoRequiredMixin, BasculaRequiredMixin
from django.shortcuts import redirect
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class BasculaView(BasculaRequiredMixin,View):
    # Renderizar la plantilla de entrada de operaciones, ademas enviar el nombre del grupo al que pertenece el usuario
    def get(self, request):
        group_name = request.user.groups.first().name
        return render(request, 'operations/entrada_operations.html', {'group_name': group_name})
    



#Importacion de modelos necesarios

from .models import Cliente
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ClienteView(BasculaRequiredMixin,View):
    # Renderizar la plantilla de clientes de operaciones, ademas enviar el nombre del grupo al que pertenece el usuario
    def get(self, request):
        
        clientes = Cliente.objects.all()
        group_name = request.user.groups.first().name
        return render(request, 'operations/cliente_operations.html', {'group_name': group_name, 'clientes':clientes})



class CrearClienteView(BasculaRequiredMixin, View):
    def post(self, request):
        # Obtener los datos del cliente
        id_cliente = request.POST.get('id_cliente')
        tipo_empresa = request.POST.get('tipo_empresa')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        nombre_empresa = request.POST.get('nombre_empresa')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        
        
        if tipo_empresa == 'false':
            tipo_empresa = False
        elif tipo_empresa == 'true':
            tipo_empresa = True
        # Crear un nuevo cliente
        cliente = Cliente(
            id_cliente=id_cliente,
            tipo_empresa=tipo_empresa,
            telefono=telefono,
            email=email,
            direccion=direccion,
            nombre_empresa=nombre_empresa,
            nombre=nombre,
            apellido=apellido
        )
        cliente.save()
        
        return redirect('clientes_operations')