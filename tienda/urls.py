from django.urls import path
from . import views

app_name = "tienda"
urlpatterns = [
    path('', views.lista, name="lista"),
    path('detalle_producto/', views.detalle, name = "detalle"),
    

]
     