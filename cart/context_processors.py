from cart.cart import Cart
from .models import CartItem

def cart_item_count(request):
    cart = Cart(request)

    if request.user.is_authenticated:
        return {'cart_item_count':sum(item.quantity for item in CartItem.objects.filter(user=request.user))}
    else:
        return {
            'cart_item_count': sum(item['quantity'] for item in cart.cart.values())
        }
