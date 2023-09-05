from django.shortcuts import render, redirect, get_object_or_404
from core.cart import Cart
from productos.models import Producto
from .forms import DireccionEnvioForm
from politicas.models import GastosEnvio

def pedidos_view(request):
    cart = Cart(request)
    cart_items = []
    total_price = 0

    for product_id, item in cart.cart.items():
        product = get_object_or_404(Producto, id=int(product_id))
        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'total_item_price': product.precio * item['quantity'],
        })

    gastos_envio = GastosEnvio.objects.first()
    subtotal = sum(item['total_item_price'] for item in cart_items)
    total = subtotal + gastos_envio.monto

    if request.method == 'POST':
        form = DireccionEnvioForm(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data['nombres_form']
            correo = form.cleaned_data['correo']
            numero_telefono = form.cleaned_data['numero_telefono']
            direccion = form.cleaned_data['direccion']

            # Realiza acciones adicionales, como crear el pedido en la base de datos, enviar correos, etc.
            
            # Limpia el carrito después de completar la compra
            # cart.clear()

            # Pasa los datos del formulario, del carrito y del resumen del pedido a la plantilla de pedidos
            context = {
                'cart_items': cart_items,
                'nombres_form': nombres,
                'correo': correo,
                'direccion': direccion,
                'numero_telefono': numero_telefono,
                'total_price': total_price,
                'gastos_envio': gastos_envio,
                'subtotal': subtotal,
                'total': total,  # Calcula el total sumando subtotal y gastos de envío
                # Otros datos necesarios para la plantilla de pedidos
            }
            return render(request, 'pedidos/pedidos.html', context)  # Muestra la página de pedidos con los datos ingresados
    else:
        form = DireccionEnvioForm()

    context = {
        'cart_items': cart_items,
        'form': form,
        'subtotal': subtotal,  # Asegúrate de incluir el subtotal aquí también
        'gastos_envio': gastos_envio,  # Asegúrate de incluir los gastos de envío aquí también
        'total': total,  # Asegúrate de incluir el total aquí también
        # Otros datos necesarios para la plantilla de pedidos
    }

    return render(request, 'pedidos/pedidos.html', context)
