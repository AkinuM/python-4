from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_waifu', views.AddWaifuView.as_view(), name='add-waifu'),
    path('<int:pk>', views.WaifuDetailView.as_view(), name='waifu-detail'),
    path('<int:pk>/delete', views.WaifuDeleteView.as_view(), name='waifu-delete'),
    path('<int:pk>/edit', views.WaifuEditView.as_view(), name='waifu-edit'),
]
