import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sree.settings')
django.setup()

from pro.models import Client, Product, QuoteRequest

# Create a test client
client, created = Client.objects.get_or_create(
    email='testcustomer@example.com',
    defaults={
        'name': 'John Smith',
        'company': 'Tech Manufacturing Inc',
        'phone': '+91-9876543210',
        'address': '123 Industrial Park, Chennai',
        'industry': 'automotive'
    }
)

print(f"Client: {client.name} ({client.company}) - {'Created' if created else 'Existing'}")

# Get a product
product = Product.objects.first()
print(f"Product: {product.name}")

# Create a quote request
quote = QuoteRequest.objects.create(
    client=client,
    product=product,
    width=500,
    height=800,
    material='stainless',
    finish='brushed',
    quantity=5,
    special_requirements='Need urgent delivery by end of month',
    status='pending'
)

print(f"\n✓ Order Created Successfully!")
print(f"Order ID: {quote.id}")
print(f"Customer: {quote.client.name}")
print(f"Company: {quote.client.company}")
print(f"Email: {quote.client.email}")
print(f"Product: {quote.product.name}")
print(f"Dimensions: {quote.width}mm x {quote.height}mm")
print(f"Quantity: {quote.quantity}")
print(f"Material: {quote.material}")
print(f"Finish: {quote.finish}")
print(f"Status: {quote.status}")
print(f"\nNow go to http://localhost:8000/admin/pro/quoterequest/ to see this order!")
