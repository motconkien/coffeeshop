from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from app_shop.models import *
from . import forms

def index(request):
    categories = Category.objects.all()
    return render(request, 'app_shop/index.html',{
                  'categories': categories})

def about(request):
    categories = Category.objects.all()
    return render(request, 'app_shop/about.html',{
                  'categories': categories})

def menu(request, category_id):
    
    categories = Category.objects.all()

    #list of products in the selected category
    # products = Product.objects.filter(category=category_id)

    #handle by get method 
    keyword = request.GET.get("tu_khoa",'')
    if keyword:
        filtered_products = Product.objects.filter(category=category_id,name__icontains=keyword)
    else:
        filtered_products = Product.objects.filter(category=category_id)
    #take name of the category
    category= Category.objects.get(id=category_id)

    #set number of products in the category
    paginator = Paginator(filtered_products, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_shop/menu.html',{
                  'categories': categories,
                #   'products': products,
                  'category': category,
                  'page_obj': page_obj,
                  'keyword':keyword
                  })

def contact(request):
    categories = Category.objects.all()

    result = ""
    
    if request.method == "POST":
        form = forms.FormContact(request.POST)
        if form.is_valid():
            form.save()  #model form will do everything
            result = 'Thank you for your contact'
            form = forms.FormContact()  # Reset form after successful submission
        else:
            result = 'There was an error in your submission'
    else:
        form = forms.FormContact() 
        
    return render(request, 'app_shop/contact.html',{
                  'categories': categories,
                  'form': form,
                'result': result})

def order(request):
    categories = Category.objects.all()
    
    #dict palceholder 
    category_products = {
        category:Product.objects.filter(category = category)[:4] for category in categories
    }
   

    return render(request, 'app_shop/order.html', {
                            'category_products': category_products
                            })