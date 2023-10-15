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
from .wishlist import Wish
from .models import Comentario
from politicas.models import Cupon
from pedidos.models import PedidosOrden

# Importaciones de Python
import random   
from politicas.models import CorreoEmpresa, BrandImage

# Importa tu formulario en las vistas




def home(request):
    ultimos_productos = Producto.objects.filter(cantidad_disponible__gt=0).order_by('-fecha_carga')[:8]
    productos_aleatorios = list(Producto.objects.filter(cantidad_disponible__gt=0))
    random.shuffle(productos_aleatorios)
    productos_aleatorios = productos_aleatorios[:8]  # Mostrar 4 productos aleatorios
    
    correo_empresa = CorreoEmpresa.objects.first()  # Obtén el primer registro de CorreoEmpresa
    # copy = Copyright.objects.first() # obten los derechos de autor
    comentarios = Comentario.objects.all()

    brand_images = BrandImage.objects.all()  # Obtén todas las imágenes de marca disponibles
    
    return render(request, "core/home.html", {
        'ultimos_productos': ultimos_productos,
        'productos_aleatorios': productos_aleatorios,
        'correo_empresa': correo_empresa,
        'comentarios':comentarios,
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


def myaccount(request):
    # Obtén los pedidos asociados al usuario actual
    pedidos_usuario = PedidosOrden.objects.filter(user=request.user)

    return render(request, "core/my-account.html", {'pedidos_usuario': pedidos_usuario})

def wishlist(request):
        return render(request, "core/wishlist.html")
def contact(request):
        return render(request, "core/contact.html")
def admin(request):
        return render(request, "core/admin.html")
def regis(request):
        return render(request, "core/regis.html")


"""
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
                       CART
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

"""

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
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)

    messages.success(request, 'El producto se ha añadido al carrito correctamente.')

    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

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
    

def move_to_cart(request, product_id):
    wish_list = Wish(request)
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    
    # Verifica si el producto está en la lista de deseos
    if str(product_id) in wish_list.wishlist:
        # Obtiene la cantidad del producto en la lista de deseos
        quantity = wish_list.wishlist[str(product_id)]['quantity']
        # Agrega el producto al carrito con la cantidad correspondiente
        cart.add(product=product, quantity=quantity)

    messages.success(request, 'El producto se ha ha movido al carritocorrectamente.')
    # Redirige al usuario de vuelta a la lista de deseos o a donde desees
    return redirect('wishlist')  # Ajusta el nombre de la vista de la lista de deseos si es diferente



"""
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡
                        WISH LIST
≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡

"""

def wish_cart(request):
    wish_list = Wish(request)
    wish_items = []

    for product_id, item_data in wish_list.wishlist.items():
        product = get_object_or_404(Producto, id=int(product_id))
        wish_items.append({
            'product': product,
        })

    return render(request, "core/wishlist.html", {
        'wish_items': wish_items,
    })


def add_to_wish(request, product_id):
    wish_list = Wish(request)
    product = get_object_or_404(Producto, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    wish_list.add(product=product, quantity=quantity)

    messages.success(request, 'El producto se ha añadido a la lista de deseos correctamente.')

    return redirect(request.META.get('HTTP_REFERER', 'home'))  # Redirige a la página anterior o la página de inicio si no hay referencia


def remove_from_wish(request, product_id):
    wish_list = Wish(request)
    product = wish_list.get_product(product_id)
    wish_list.remove(product_id)

    messages.success(request, 'El producto se ha eliminado de la lista de deseos correctamente.')
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    else:
        return redirect('core:wishlist')  # Cambiado el redireccionamiento a la página de la lista de deseos