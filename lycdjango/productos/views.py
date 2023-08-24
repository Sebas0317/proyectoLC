from django.core.paginator import Paginator
from django.shortcuts import render
from productos.models import Producto
from politicas.models import BrandImage
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
        price_ranges = {
            '0-20000': (0, 20000),
            '20000-40000': (20000, 40000),
            '40000-60000': (40000, 60000),
            '60000-80000': (60000, 80000),
            '80000-100000': (80000, 100000),
            '100000': (100000, None),
        }
        price_range = price_ranges.get(precio)
        if price_range:
            productos = productos.filter(precio__range=price_range)

    paginator = Paginator(productos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    producto_aleatorio = random.choice(productos)

    brand_images = BrandImage.objects.all()

    return render(request, 'productos/product_list.html', {
        'page_obj': page_obj,
        'producto_aleatorio': producto_aleatorio,
        'filtro': filtro,
        'precio': precio,
        'brand_images': brand_images,
    })
