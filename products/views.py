from django.http import HttpResponse
from django.shortcuts import render

from .admin import OfferAdmin
from .models import Product


def index(request):
    Products = Product.objects.all()
    return render(request, 'index.html', {'products': Products})


def new(request):
    return HttpResponse('new')

