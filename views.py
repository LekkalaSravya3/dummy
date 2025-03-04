from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
#products -> index
#Uniform Resource locator (Address)
def index(request):
    
    return render(request,'index.html')
def new(request):
    return HttpResponse('New Products')

# Create your views here.
