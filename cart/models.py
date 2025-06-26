from django.db import models
from app_shop.models import Product
# Create your models here.

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    #add product 
    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': quantity,
                'image': product.image.url,
            }
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    #remove product 
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True
    
    #clear 
    def clear(self):
        self.session['cart'] = {}
        self.save()
    
    def __iter__(self):
        product_ids = [int(pid) for pid in self.cart.keys()]
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            item = self.cart[str(product.id)]
            item['product'] = product
            item['subtotal'] = float(item['price']) * item['quantity']
            yield item

    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
