from django.urls import path
from .views import *

app_name = 'app_shop'
urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('menu/<int:category_id>/',menu,name='menu'),
    path('contact/',contact,name='contact'),
    path('order/', order, name='order')
]
