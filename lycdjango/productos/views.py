from django.core.paginator import Paginator
from django.shortcuts import render
from productos.models import Producto
import random

def product_list(request):
    # Obtener todos los productos y ordenarlos por ID (puedes cambiarlo según tus necesidades)
    productos = Producto.objects.order_by('id')

    paginator = Paginator(productos, 9)  # Crea un objeto Paginator y establece 9 productos por página
    page_number = request.GET.get('page')  # Obtiene el número de página actual desde la URL

    page_obj = paginator.get_page(page_number)  # Obtiene los productos de la página actual

    # Obtener un producto aleatorio entre los productos de la página actual
    producto_aleatorio = random.choice(page_obj)

    return render(request, 'productos/product_list.html', {'page_obj': page_obj, 'producto_aleatorio': producto_aleatorio})
