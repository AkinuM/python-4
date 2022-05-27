from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.aboba, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]