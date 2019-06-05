from django.shortcuts import render,get_object_or_404 
from .models import ProductType, Product, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

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
    reviews=Review.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviews' : reviews,
    }
    return render(request, 'techapp/productdetails.html', context=context)

@login_required
def newproduct(request):
    form=ProductForm
    if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
    else:
          form=ProductForm()
    return render(request, 'techapp/newproduct.html', {'form': form})

@login_required
def newreview(request):
    form=ReviewForm
    if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
    else:
          form=ReviewForm()
    return render(request, 'techapp/newreview.html', {'form': form})

def loginmsg(request):
      return render(request, 'techapp/loginmsg.html')

def logoutmsg(request):
      return render(request, 'techapp/logoutmsg.html')

