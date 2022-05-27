from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.db, name='db_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PegsDetailView.as_view(), name='db-detail'),
    path('<int:pk>/update', views.PegsUpdateView.as_view(), name='db-update'),
    path('<int:pk>/delete', views.PegsDeleteView.as_view(), name='db-delete'),
    path('register', views.RegisterView.as_view(), name='register'),
]