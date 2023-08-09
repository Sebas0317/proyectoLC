# Importaciones de Django
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

# Importaciones del proyecto
from productos.models import Producto
from .cart import Cart

# Importaciones de Python
import random   

def home(request):
    ultimos_productos = Producto.objects.filter(cantidad_disponible__gt=0).order_by('-fecha_carga')[:4]
    productos_aleatorios = list(Producto.objects.filter(cantidad_disponible__gt=0))
    random.shuffle(productos_aleatorios)
    productos_aleatorios = productos_aleatorios[:4]  # Mostrar 4 productos aleatorios
    
    return render(request, "core/home.html", {
        'ultimos_productos': ultimos_productos,
        'productos_aleatorios': productos_aleatorios,
    })


def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    productos_relacionados = Producto.objects.filter(tipo=producto.tipo).exclude(id=producto_id)[:4]
    productos = Producto.objects.all().exclude(id=producto_id)
    producto_aleatorio = random.choice(productos)
    
    return render(request, 'core/product-detail.html', {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'producto_aleatorio': producto_aleatorio,
    })


def productlist(request):
        return render(request, "core/product-list.html")

def checkout(request):
        return render(request, "core/checkout.html")
def myaccount(request):
        return render(request, "core/my-account.html")
def wishlist(request):
        return render(request, "core/wishlist.html")
def contact(request):
        return render(request, "core/contact.html")
def admin(request):
        return render(request, "core/admin.html")
def regis(request):
        return render(request, "core/regis.html")
def product_cart(request):
    cart = Cart(request)
    cart_items = []
    total_price = 0

    for product_id, item_data in cart.cart.items():
        product = get_object_or_404(Producto, id=int(product_id))
        quantity = item_data['quantity']
        total_item_price = product.precio * quantity
        total_price += total_item_price
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_item_price': total_item_price,
            # 'imagen': product.imagen.url,  # Agregar la URL de la imagen al diccionario
        })

    return render(request, "core/cart.html", {
        'cart_items': cart_items, 
        'total_price': total_price
        })
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Obtener la cantidad del campo de entrada
    cart.add(product=product, quantity=quantity)

    # Agregar el mensaje flash
    messages.success(request, 'El producto se ha añadido al carrito correctamente.')

    # Verificar si la solicitud proviene de la página de detalles del producto
    referer = request.META.get('HTTP_REFERER', '/')
    if 'product_detail' in referer:
        return redirect(referer)  # Redirigir a la página de detalles del producto
    else:
        return redirect('product_detail', producto_id=product_id)  # Redirigir a la página de inicio o a la página del carrito.


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = cart.get_product(product_id)
    cart.remove(product_id)  # Corrección: pasar el product_id en lugar del objeto product

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True
            })
    else:
        return redirect('core/cart.html')
    
def add_to_cart_product_list(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Obtener la cantidad del campo de entrada

    # Intentar agregar el producto al carrito
    added_to_cart = cart.add(product=product, quantity=quantity)

    # Devolver una respuesta JSON con el resultado
    return JsonResponse({'added_to_cart': added_to_cart})
    
