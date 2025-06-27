from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from app_order.models import Order, OrderItem
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


# def create_order(request):
#     cart = Cart(request)

#     if not any(cart):
#         messages.warning(request,"Empty")
#         return redirect('app_cart:cart_view')
    
#     #if cart 
#     order = Order.objects.create(
#         user = request.user,
#         total_price = cart.get_total_price()
#     )

#     for item in cart:
#         OrderItem.objects.create(
#             order=order,
#             product = item['product'],
#             price=item['product'].price,
#             quantity=item['quantity']
#         )
#     cart.clear()
#     messages.success(request,"Order successfully")
#     return redirect('order:order_success')



def checkout_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.total_price = cart.get_total_price()
            order.save()

            for item in cart:
                OrderItem.objects.create(
            order=order,
            product = item['product'],
            price=item['product'].price,
            quantity=item['quantity']
            )
            cart.clear()

            send_mail(
                subject=f'Order Confirmation #{order.pk}',
                message=f'Thank you for your order, {order.full_name}!\nYour order ID is {order.pk}.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[order.email],
                fail_silently=False,
            )
            return redirect('order:order_success')
    else:
        form = CheckoutForm()
    return render(request, 'order/checkout.html', {'form': form, 'cart': cart})


def order_success(request):
    return render(request, 'order/order_success.html')