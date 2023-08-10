from django.core.paginator import Paginator
from django.shortcuts import render
from productos.models import Producto
import random

def product_list(request):
    filtro = request.GET.get('filtro', '')
    precio = request.GET.get('precio', '')

    productos = Producto.objects.all()

    if filtro == 'reciente':
        productos = productos.order_by('-fecha_carga')
    elif filtro == 'popular':
        productos = random.sample(list(productos), len(productos))
    elif filtro == 'masvendidos':
        productos = productos.order_by('-cantidad_disponible')

    if precio:
        if precio == '0-20000':
            productos = productos.filter(precio__range=(0, 20000))
        elif precio == '20000-40000':
            productos = productos.filter(precio__range=(20000, 40000))
        elif precio == '40000-60000':
            productos = productos.filter(precio__range=(40000, 60000))
        elif precio == '60000-80000':
            productos = productos.filter(precio__range=(60000, 80000))
        elif precio == '80000-100000':
            productos = productos.filter(precio__range=(80000, 100000))
        elif precio == '100000':
            productos = productos.filter(precio__gte=100000)

    paginator = Paginator(productos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    producto_aleatorio = random.choice(productos)

    return render(request, 'productos/product_list.html', {
        'page_obj': page_obj,
        'producto_aleatorio': producto_aleatorio,
        'filtro': filtro,
        'precio': precio,
    })


