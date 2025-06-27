from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('success/', views.order_success, name='order_success'),
    path('checkout/', views.checkout_view, name='checkout'),

]