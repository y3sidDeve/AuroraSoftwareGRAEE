from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden

class GroupRequiredMixin(AccessMixin):
    allowed_groups = []

    def handle_no_permission(self):
        # Redirigir al usuario a una página de acceso denegado o mostrar un mensaje de error
        response = HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        response['Refresh'] = '3;url=/salir/'  # Redirigir después de 3 segundos
        return response

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not any(request.user.groups.filter(name=group) for group in self.allowed_groups):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class TecnicoRequiredMixin(GroupRequiredMixin):
    allowed_groups = ['Técnico']

class BasculaRequiredMixin(GroupRequiredMixin):
    allowed_groups = ['Báscula']

