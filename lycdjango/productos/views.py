from django.core.paginator import Paginator
from django.shortcuts import render
from productos.models import Producto
import random

def product_list(request):
    filtro = request.GET.get('filtro', '') 

    productos = Producto.objects.all()

    if filtro == 'reciente':
        productos = productos.order_by('-fecha_carga')
    elif filtro == 'popular':
        productos = random.sample(list(productos), len(productos))
    elif filtro == 'masvendidos':
        productos = productos.order_by('-cantidad_disponible')

    paginator = Paginator(productos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    producto_aleatorio = random.choice(productos)

    return render(request, 'productos/product_list.html', {
        'page_obj': page_obj,
        'producto_aleatorio': producto_aleatorio,
        'filtro': filtro  # Pasa el filtro seleccionado al contexto
    })

