from django.shortcuts import render, redirect, get_object_or_404
from core.cart import Cart
from productos.models import Producto
from .forms import DireccionEnvioForm
from politicas.models import GastosEnvio
# Importa el modelo Pedido desde la aplicación pedidos
from pedidos.models import Pedido

# Resto de tu vista
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

            # Crea un objeto Pedido y guárdalo en la base de datos
            for item in cart_items:
                producto = item['product']
                cantidad = item['quantity']
                total_compra = item['total_item_price']

                pedido = Pedido(
                    nombres=nombres,
                    correo=correo,
                    numero_telefono=numero_telefono,
                    direccion=direccion,
                    producto=producto,
                    cantidad=cantidad,
                    total_compra=total_compra
                )
                pedido.save()

            # Limpia el carrito después de completar la compra
            # cart.clear()

            # Redirige al usuario a la página de confirmación o donde desees
            return redirect('confirmacion')

    else:
        form = DireccionEnvioForm()

    context = {
        'cart_items': cart_items,
        'form': form,
        'subtotal': subtotal,
        'gastos_envio': gastos_envio,
        'total': total,
        # Otros datos necesarios para la plantilla de pedidos
    }

    return render(request, 'pedidos/pedidos.html', context)

def confirmacion_view(request):
    # Lógica de confirmación de pedidos aquí
    pedido = Pedido.objects.all()
    context = {'pedido': pedido}
    return render(request, 'pedidos/confirmacion.html', context)