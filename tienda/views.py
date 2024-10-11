from django.shortcuts import render

# Create your views here.
def lista(request):
    return render(request, "tienda/lista_productos.html")


def detalle(request):
    return render(request, "tienda/detalle_producto.html")



