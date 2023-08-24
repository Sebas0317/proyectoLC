# wishlist.py
from django.apps import apps

class Wish:
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get("wishlist")
        if not wishlist:
            wishlist = self.session["wishlist"] = {}
        self.wishlist = wishlist

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product_id] = {
                "quantity": quantity,
                "price": product.precio,  # Sin convertir a cadena
            }
        else:
            self.wishlist[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product_id):
        product_id_str = str(product_id)
        if product_id_str in self.wishlist:
            del self.wishlist[product_id_str]
            self.save()
            
    def get_product(self, product_id):
        product_model = apps.get_model('productos', 'Producto')
        return product_model.objects.get(id=product_id)
    def save(self):
        self.session['wishlist'] = self.wishlist
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.wishlist.values())
