from django.shortcuts import render, redirect, get_object_or_404
from core.cart import Cart
from productos.models import Producto
from .forms import DireccionEnvioForm
from politicas.models import GastosEnvio
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


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

    gastos_envio = GastosEnvio.objects.first()
    subtotal = sum(item['total_item_price'] for item in cart_items)
    total = subtotal + gastos_envio.monto

    nombres = ''
    correo = ''
    direccion = ''
    numero_telefono = ''

    if request.method == 'POST':
        form = DireccionEnvioForm(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data['nombres_form']
            correo = form.cleaned_data['correo']
            numero_telefono = form.cleaned_data['numero_telefono']
            direccion = form.cleaned_data['direccion']

    else:
        form = DireccionEnvioForm(request.user)

    context = {
        'cart_items': cart_items,
        'form': form,
        'subtotal': subtotal,
        'gastos_envio': gastos_envio,
        'total': total,
        'nombres_form': nombres,
        'correo': correo,
        'numero_telefono': numero_telefono,
        'direccion': direccion,
    }

    return render(request, 'pedidos/pedidos.html', context)


# def send_email(request,cart_items, nombres, correo, numero_telefono, direccion):
#     # Enviar correo
#     subject = 'Confirmación de pedido'
#     message = f'Ud ha comprado los siguientes artículos:\n'
#     for item in cart_items:
#         message += f'{item["product"].nombre} - Cantidad: {item["quantity"]}\n'
#     message += f'\nLos artículos han sido enviados con los siguientes datos:\n'
#     message += f'Nombres: {nombres}\nCorreo: {correo}\nTeléfono: {numero_telefono}\nDirección: {direccion}'

#     send_mail(subject, message, 'comercializadoralyc99@gmail.com', [correo])
#     return render(request, 'pedidos/pedidos.html')


def send_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("pedidos/confirmacion.html",{
        'cart_items': kwargs.get('cart_items'),
        'form': kwargs.get('form'),
        'subtotal': kwargs.get('subtotal'),
        'gastos_envio': kwargs.get('gastos_envio'),
        'total': kwargs.get('total'),
        'nombres_form': kwargs.get('nombres'),
        'correo': kwargs.get('correo'),
        'numero_telefono': kwargs.get('numero_telefono'),
        'direccion': kwargs.get('direccion')
        })

    mensaje_texto=strip_tags(mensaje) ##variable que es igual a la otra variable de mensaje pero ingnorando las etiquetas html de la ubucacion del archivo
    from_email="comercializadoralyc99@gmail.com"
    to=kwargs.get("correo")
    #to="victordanielmar91@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)


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
            'total_item_price': total_item_price, })
    gastos_envio = GastosEnvio.objects.first()
    subtotal = total_price
    total = total_price + gastos_envio.monto

    return render(request, "pedidos/checkout.html", {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'gastos_envio': gastos_envio,
        'total': total,
    })
