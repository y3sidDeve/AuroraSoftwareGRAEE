"""
URL configuration for aurora_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from session.views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', include('home.urls')), #pagina principal
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', CustomLoginView.as_view(), name='custom_login'),
    path('salir/', include('session.urls'), name='logout'), #cerrar sesion
    
    
    #enrutamiento a las aplicaciones
    path('home/', include('home.urls')),
    path('operations/', include('operations.urls')),
    path('crc/', include('crc.urls')),
]