from django.shortcuts import render, redirect
from .models import Contact, Order, Reserve

# --- Frontend Pages ---

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def order(request):
    return render(request, 'order.html')

def reserve(request):
    return render(request, 'reserve.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Save to database
        contact_entry = Contact(name=name, email=email, message=message)
        contact_entry.save()
        
    return render(request, 'contact.html')

        
    return render(request, 'contact.html')


# --- Dashboard / Admin Pages ---

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def show_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'dashboard/show_contact.html', {'contacts': contacts})


def show_order(request):
    all_orders = Order.objects.all()
    return render(request, 'dashboard/show_order.html', {'data': all_orders})


def show_reserve(request):
    all_reserves = Reserve.objects.all()
    return render(request, 'dashboard/show_reserve.html', {'data': all_reserves})
