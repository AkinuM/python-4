from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.db, name='db_home'),
]