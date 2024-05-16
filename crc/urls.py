from django.urls import path
from django.urls import include
from crc.views import InicioView

urlpatterns = [
    path('dashboard-crc/', InicioView.as_view(), name='dashboard_crc'),
]