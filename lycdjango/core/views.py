# Importaciones de Django
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from politicas.models import GastosEnvio
# Importaciones del proyecto
from productos.models import Producto
from .cart import Cart
from politicas.models import Cupon

# Importaciones de Python
import random   
from politicas.models import CorreoEmpresa,BrandImage,Copyright


def home(request):
    ultimos_productos = Producto.objects.filter(cantidad_disponible__gt=0).order_by('-fecha_carga')[:8]
    productos_aleatorios = list(Producto.objects.filter(cantidad_disponible__gt=0))
    random.shuffle(productos_aleatorios)
    productos_aleatorios = productos_aleatorios[:8]  # Mostrar 4 productos aleatorios
    
    correo_empresa = CorreoEmpresa.objects.first()  # Obtén el primer registro de CorreoEmpresa
    copy = Copyright.objects.first() # obten los derechos de autor

    brand_images = BrandImage.objects.all()  # Obtén todas las imágenes de marca disponibles
    
    return render(request, "core/home.html", {
        'ultimos_productos': ultimos_productos,
        'productos_aleatorios': productos_aleatorios,
        'correo_empresa': correo_empresa,
        #'copy': copy,
        'brand_images': brand_images,  # Agrega las imágenes de la marca al contexto
    })

def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    productos_relacionados = Producto.objects.filter(tipo=producto.tipo).exclude(id=producto_id)[:8]
    productos_disponibles = Producto.objects.all().exclude(id=producto_id)
    
    productos_aleatorios = random.sample(list(productos_disponibles), len(productos_relacionados))
    
    brand_images = BrandImage.objects.all()  # Obtén todas las imágenes de marca disponibles
    
    return render(request, 'core/product-detail.html', {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'productos_aleatorios': productos_aleatorios,
        'brand_images': brand_images,
    })




def productlist(request):
    correo_empresa = CorreoEmpresa.objects.first()  # Obtén el primer registro de CorreoEmpresa
    return render(request, "core/product-list.html",{
            'correo_empresa': correo_empresa,
        }) 

def checkout(request):
    user = request.user
    cart = Cart(request)
    cart_items = []
    total_price = 0

    for product_id, item_data in cart.cart.items():
        product = get_object_or_404(Producto, id=int(product_id))
        quantity = item_data['quantity']
        total_item_price = product.precio * quantity
        total_price += total_item_price
        cart_items.append({
            'user': user,
            'product': product,
            'quantity': quantity,
            'total_item_price': total_item_price,
        })

    gastos_envio = GastosEnvio.objects.first()
    subtotal = total_price
    total = total_price + gastos_envio.monto

    return render(request, "core/checkout.html", {
        'cart_items': cart_items,
        'total_price': total_price,
        'gastos_envio': gastos_envio,
        'subtotal': subtotal,
        'total': total,
    })
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
        })
        
    gastos_envio = GastosEnvio.objects.first()
    subtotal = total_price

    # cupon_codigo = request.POST.get('cupon_codigo')  # Obtiene el código del cupón del formulario

    # descuento = 0  # Inicializa el descuento en 0
    # if cupon_codigo:
    #     try:
    #         cupon = Cupon.objects.get(codigo=cupon_codigo)
    #         descuento = cupon.descuento
    #         total_price -= total_price * (descuento / 100)  # Aplica el descuento al total_price
    #     except Cupon.DoesNotExist:
    #         pass

    total = total_price + gastos_envio.monto  # Calcula el total sumando total_price y gastos de envío
    # descuento_total = total_price * (descuento / 100)  # Calcula el descuento total

    return render(request, "core/cart.html", {
        'cart_items': cart_items,
        'total_price': total_price,
        'gastos_envio': gastos_envio,
        'subtotal': subtotal,
        'total': total,
        # 'descuento_total': descuento_total,
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
    
def add_to_cart_home(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    quantity = 1  # Establecer la cantidad
    cart.add(product=product, quantity=quantity)

    # Agregar el mensaje flash
    messages.success(request, 'El producto se ha añadido al carrito correctamente.')

    return redirect('home')  # Redirigir a la página de inicio


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
    
def update_cart_quantity(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_quantity = int(request.POST.get('new_quantity'))
        
        cart = Cart(request)  # Assuming you have your Cart class defined
        cart.update_quantity(product_id, new_quantity)
        
        product = cart.get_product(product_id)
        total_item_price = product.precio * new_quantity
        
        response_data = {
            'total_item_price': total_item_price,
        }
        
        return JsonResponse(response_data)
    
def add_to_cart_product_list(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Obtener la cantidad del campo de entrada

    # Intentar agregar el producto al carrito
    added_to_cart = cart.add(product=product, quantity=quantity)

    # Devolver una respuesta JSON con el resultado
    return JsonResponse({'added_to_cart': added_to_cart})
    
