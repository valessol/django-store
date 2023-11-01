from django.shortcuts import render, redirect
from store.models import Product, Cart, Query
from store.forms import ContactForm

def initialize(request):
    return render(request, 'store/index.html', {})


def products(request): 
    search = request.GET.get('search')
    
    if search:
        products_list = Product.objects.filter(name__icontains=search)
    else:
        products_list = Product.objects.all()
        
    return render(request, 'store/products.html', {'products_list': products_list})


def add_item(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.POST.get('image')
        
        product = Product(name=name, description=description, price=price, stock=stock, image=image)
        product.save()
        return redirect('productos')
    
    
    return render(request, 'store/add_item.html', {})

def add_to_cart(request): 
    if request.method == 'POST':
        client = request.POST.get('client')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        
        cart = Cart(client=client, product=product, quantity=quantity)
        cart.save()
        return redirect('inicio')
    # TODO: si el cart ya existe, agregar los productos
    return render(request, 'store/add_to_cart.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nombre_de_contacto = data.get('nombre_de_contacto')
            consulta = data.get('consulta')
            telefono = data.get('telefono')
            
            query = Query(nombre_de_contacto=nombre_de_contacto, consulta=consulta,telefono=telefono)
            query.save()
            
            return redirect('inicio')
        else: 
            return render(request, 'store/contact.html', {'form': form})
        
    form = ContactForm()
    return render(request, 'store/contact.html', {'form': form})