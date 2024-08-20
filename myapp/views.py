from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    return render(request,'index,html')

def product(request):
    product_data = Product.objects.all()   # this is a qurery of orm  (oject relational mapping)
    # print(product_data,"product data")
    context = {
        'product':product_data
    }
    return render(request,'Product.html',context)
    