from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('detalle/', views.detalle, name='detalle'),
]