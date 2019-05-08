from django.shortcuts import *
from .models import ProductType, Product, Review

# Create your views here.
def index (request):
    return render(request, 'techapp/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'techapp/types.html' ,{'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'techapp/products.html', {'products_list': products_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'techapp/productdetails.html', context=context)