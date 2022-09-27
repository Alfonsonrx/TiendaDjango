from django.shortcuts import render
from .models import Product, Comment

# Create your views here.
def index(request):
    latest_product_list = Product.objects.all()
    return render(request, 'catalogo/index.html', {
        'latest_product_list': latest_product_list
    })