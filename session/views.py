from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


from django.contrib.auth.models import Group
# Create your views here.


class CustomLoginView(LoginView):
    def get_success_url(self):
        # Obtener el usuario actualmente autenticado
        user = self.request.user

        # Verificar el grupo al que pertenece el usuario y redirigir al dashboard correspondiente
        if user.groups.filter(name='Técnico').exists():
            return reverse_lazy('dashboard_crc')
        elif user.groups.filter(name='Báscula').exists():
            return reverse_lazy('dashboard_operations')
        else:
            # Si el usuario no pertenece a ningún grupo específico, redirigir a una URL predeterminada
            return reverse_lazy('default_dashboard')



@login_required
def salir(request):
    logout(request)
    return redirect('/')
