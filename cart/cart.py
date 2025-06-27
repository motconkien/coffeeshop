from django.db import models
from app_shop.models import Product
from cart.models import CartItem

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.user = request.user
        self.is_authenticated = request.user.is_authenticated
        self.session_cart = request.session.get("cart",{})
        self.cart = self.session_cart
    
    #add product 
    def add(self, product, quantity=1):
        if self.is_authenticated:
            item,created = CartItem.objects.get_or_create(user=self.user, product=product)
            if not created:
                item.quantity += quantity
                item.save()
        else:
            product_id = str(product.id)
            if product_id in self.session_cart:
                self.session_cart[product_id]['quantity'] += quantity
            else:
                self.session_cart[product_id] = {
                    'name': product.name,
                    'price': str(product.price),
                    'quantity': quantity,
                    'image': product.image.url,
                }
                self.session['cart'] = self.session_cart
                self.save()

    #remove product 
    def remove(self, product):
        if self.is_authenticated:
            CartItem.objects.filter(user=self.user, product=product).delete()
        else:
            product_id = str(product.id)
            if product_id in self.cart:
                del self.cart[product_id]
                self.save()

    def save(self):
        self.session.modified = True
    
    #clear 
    def clear(self):
        if self.is_authenticated:
            items = CartItem.objects.filter(user=self.user)
            items.delete()
        self.session['cart'] = {}
        self.save()
    
    def __iter__(self):
        if self.is_authenticated:
            items = CartItem.objects.filter(user=self.user)
            for item in items:
                yield {
                    'product': item.product,
                    'quantity': item.quantity,
                    'subtotal': item.subtotal()
                }
        else:
            product_ids = self.session_cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            for product in products:
                item = self.session_cart[str(product.id)]
                yield {
                    'product': product,
                    'quantity': item['quantity'],
                    'subtotal': float(item['price']) * item['quantity']
                }

    
    def get_total_price(self):
        return sum(item['subtotal'] for item in self)
    
    def merge_session_cart_to_user(self):
        """
        Merge the session cart items into the authenticated user's CartItems
        and then clear the session cart
        """
        if not self.is_authenticated:
            return
        
        for product_id, item in self.session_cart.items():
            product = Product.objects.get(id=product_id)
            cart_item,created = CartItem.objects.get_or_create(user=self.user, product=product)

            if not created:
                cart_item.quantity += item['quantity']
            else:
                cart_item.quantity = item['quantity']
            cart_item.save()
        self.session['cart'] = {}
        self.save()