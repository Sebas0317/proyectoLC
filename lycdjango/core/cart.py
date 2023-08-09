# cart.py
from django.apps import apps

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": quantity,
                "price": product.precio,  # Sin convertir a cadena
            }
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product_id):
        product_id_str = str(product_id)
        if product_id_str in self.cart:
            del self.cart[product_id_str]
            self.save()
            
    def update_quantity(self, product_id, new_quantity):
        product_id_str = str(product_id)
        if product_id_str in self.cart:
            self.cart[product_id_str]['quantity'] = new_quantity
            self.save()
            
    def get_product(self, product_id):
        product_model = apps.get_model('productos', 'Producto')
        return product_model.objects.get(id=product_id)
    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
