from django.db import models
from django.contrib.auth.models import User
from app_shop.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=(
        ('COD', 'Cash on Delivery'),
        ('BANK', 'Bank Transfer'),
        # ('MOMO', 'Momo'), ...
    ))
    total_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username if self.user else 'Anonymous'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        return self.price*self.quantity