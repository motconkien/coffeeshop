from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from cart.models import *
from cart.cart import *
from django.contrib import messages
from django.views.decorators.http import require_POST


# Create your views here.
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product=product)
    print("Current cart contents:", request.session.get("cart"))
    messages.success(request, f"{product.name} added to cart!")
    return redirect(request.META.get('HTTP_REFERER', 'app_shop:order'))

def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {
        'cart': cart,
        'total_price': cart.get_total_price(),
    })

#update cart 
@require_POST
def update_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    current_quantity = cart.cart.get(str(product_id),{}).get('quantity',1)
    action = request.POST.get('action')

    if action == 'increase':
        current_quantity +=1
    elif action == 'decrease':
        current_quantity = max(1,current_quantity-1)
    else:
        try:
            current_quantity = int(request.POST.get('quantity', current_quantity))
        except Exception as e:
            current_quantity = current_quantity
    
    cart.cart[str(product.id)]['quantity'] = current_quantity
    cart.save()
    return redirect('app_cart:cart_view')

#remove item
@require_POST
def remove_item(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f"Removed {product.name} from cart.")
    return redirect('app_cart:cart_view')