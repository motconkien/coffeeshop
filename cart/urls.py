from django.urls import path
from . import views

app_name = 'app_cart'
urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_view, name='cart_view'), 
    path('update/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('remove/<int:product_id>/', views.remove_item, name='remove_item'),

]