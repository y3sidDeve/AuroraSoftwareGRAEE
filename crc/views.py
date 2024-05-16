from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from session.mixins import BasculaRequiredMixin, TecnicoRequiredMixin

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class InicioView(TecnicoRequiredMixin, View):
    def get(self, request):
        group_name = request.user.groups.first().name
        return render(request, 'crc/inicio_crc.html', {'group_name': group_name})



