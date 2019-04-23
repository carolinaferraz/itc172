from django.shortcuts import render
from .models import Resource


# Create your views here.
def index (request):
    return render(request, 'club/index.html')

#resources 
def getresources(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})