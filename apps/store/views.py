from django.shortcuts import render

def home (request):
    return render(request,'base/base.html')

def contact (request):
    return render(request,'paginas/contact.html')

def abaut (request):
    return render(request,'paginas/abaut.html')


def services (request):
    return render(request,'paginas/services.html')


def login (request):
    return render(request,'paginas/login.html')

    
def factura (request):
    return render(request,'paginas/factura.html')

    
def checkout (request):
    return render(request,'paginas/checkout.html')

def cart (request):
    return render(request,'paginas/cart.html')

