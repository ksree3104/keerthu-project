from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Client, QuoteRequest, FabricationProcess, MaterialAdvisor
from .forms import QuoteRequestForm, ClientForm
from .email_utils import send_quote_confirmation_email, send_contact_confirmation_email

def home(request):
    all_products = Product.objects.all().order_by('-created_at')
    featured_product = all_products.first() if all_products.exists() else None
    products = all_products
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
            # Send confirmation email to client
            send_contact_confirmation_email(client.email, client.name)
            messages.success(request, f'Thank you {client.name}! We will contact you soon.')
            return redirect('contact')
    else:
        form = ClientForm()
    return render(request, "contact.html", {'form': form})


def contact_new(request):
    """Render a standalone contact page (duplicate of contact.html) used for alternate layout or testing.
    This version simply serves the pre‑styled template without form context; form handling remains
    on the original `/contact/` view.
    """
    return render(request, "contact_new.html")

def request_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            try:
                # Get client information from form
                client_id = form.cleaned_data.get('client')
                
                if client_id:
                    # Use existing client
                    client = Client.objects.get(id=client_id)
                else:
                    # Create new client from form data
                    client_name = form.cleaned_data.get('client_name')
                    client_email = form.cleaned_data.get('client_email')
                    client_phone = form.cleaned_data.get('client_phone')
                    client_company = form.cleaned_data.get('client_company')
                    client_address = form.cleaned_data.get('client_address', '')
                    client_industry = form.cleaned_data.get('client_industry', 'other')
                    
                    # Check if client with same email exists
                    existing_client = Client.objects.filter(email=client_email).first()
                    if existing_client:
                        client = existing_client
                    else:
                        # Create new client
                        client = Client.objects.create(
                            name=client_name,
                            email=client_email,
                            phone=client_phone,
                            company=client_company,
                            address=client_address,
                            industry=client_industry
                        )
                
                # Create the quote request with the client
                quote = form.save(commit=False)
                quote.client = client
                quote.save()
                
                # Send confirmation email to client (non-blocking)
                try:
                    send_quote_confirmation_email(
                        client_email=client.email,
                        client_name=client.name,
                        product_name=quote.product.name,
                        quote_id=quote.id
                    )
                except Exception as e:
                    # Log email error but don't fail the quote submission
                    print(f"Email sending error: {e}")
                
                # Redirect to success page with quote details
                return render(request, 'order_success.html', {
                    'quote_id': quote.id,
                    'client_email': client.email,
                    'client_name': client.name
                })
            except Exception as e:
                # Handle any unexpected errors
                messages.error(request, f'An error occurred while processing your request: {str(e)}')
                return render(request, "request_quote.html", {'form': form, 'products': Product.objects.all()})
        else:
            # Form is not valid, display errors
            return render(request, "request_quote.html", {'form': form, 'products': Product.objects.all()})
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
