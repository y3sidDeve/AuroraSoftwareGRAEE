from django.urls import path
from django.urls import include
from home.views import HomeView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]