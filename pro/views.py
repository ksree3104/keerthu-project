from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Client, QuoteRequest, FabricationProcess, MaterialAdvisor
from .forms import QuoteRequestForm, ClientForm

def home(request):
    all_products = Product.objects.all()
    featured_product = all_products.first()  # Get first product as featured
    products = all_products[:5]  # Show latest 5 products
    return render(request, "3d.html", {'products': products, 'featured_product': featured_product})

def about(request):
    return render(request, "about_us.html")

def expertise(request):
    processes = FabricationProcess.objects.all()
    return render(request, "expertise.html", {'processes': processes})

def clients(request):
    clients_list = Client.objects.all().order_by('-created_at')
    return render(request, "clients.html", {'clients': clients_list})

def credentials(request):
    return render(request, "crenditail.html")

def contact(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, f'Thank you {client.name}! We will contact you soon.')
            return redirect('contact')
    else:
        form = ClientForm()
    return render(request, "contact.html", {'form': form})

def request_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            messages.success(request, 'Quote request submitted successfully! We will contact you within 24 hours.')
            return redirect('home')
    else:
        form = QuoteRequestForm()
    products = Product.objects.all()
    return render(request, "request_quote.html", {'form': form, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    products = Product.objects.all()[:4]  # Get 4 products for related products section
    return render(request, "product_detail.html", {'product': product, 'products': products})

def material_advisor(request):
    advisors = MaterialAdvisor.objects.all()
    return render(request, "material_advisor.html", {'advisors': advisors})
