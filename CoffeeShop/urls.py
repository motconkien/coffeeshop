"""
URL configuration for CoffeeShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app_shop import views as shop_views
from django.contrib.auth.views import LogoutView
from app_shop.views import CustomLogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_shop.urls')),
    path('cart/', include('cart.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='app_shop:index'), name='logout'),
    path('register/', shop_views.register, name='register'),
    path('order/', include('app_order.urls'))
]
# This file is part of the CoffeeShop project.
# It defines the URL patterns for the project, including the admin interface and the app_shop application.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)