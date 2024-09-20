from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()  # Consultar todos los productos
    return render(request, 'productos_list.html', {'productos': productos})
