from django.shortcuts import render

def initialize(request):
    return render(request, 'main/index.html', {})


def products(request): 
    return render(request, 'main/products.html', {})