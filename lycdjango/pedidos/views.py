from django.shortcuts import render, redirect, get_object_or_404
from core.cart import Cart
from productos.models import Producto
from .forms import DireccionEnvioForm

def pedidos_view(request):
    cart = Cart(request)
    cart_items = []

    for product_id, item in cart.cart.items():
        product = get_object_or_404(Producto, id=int(product_id))
        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'total_item_price': product.precio * item['quantity'],
        })

    if request.method == 'POST':
        form = DireccionEnvioForm(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data['nombres_form']
            correo = form.cleaned_data['correo']
            numero_telefono = form.cleaned_data['numero_telefono']
            direccion = form.cleaned_data['direccion']

            # Realiza acciones adicionales, como crear el pedido en la base de datos, enviar correos, etc.

            context = {
                'cart_items': cart_items,
                'nombres': nombres,
                'correo': correo,
                'direccion': direccion,
                'telefono': numero_telefono,
                # Otros datos necesarios para la plantilla
            }
            return render(request, 'pedidos/confirmacion.html', context)
    else:
        form = DireccionEnvioForm()

    context = {
        'cart_items': cart_items,
        'form': form,
        # Otros datos necesarios para la plantilla
    }

    return render(request, 'pedidos/pedidos.html', context)
