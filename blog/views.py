from django.shortcuts import render

def lista(request):
    return render(request,'lista_blog.html')

def detalle(request):
    return render(request,'detalle_comida.html')
# Create your views here.
