from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View

# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')
    
    
