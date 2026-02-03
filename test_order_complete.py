import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sree.settings')
django.setup()

from pro.models import Client, Product, QuoteRequest

print("="*70)
print(" TEST: Order Placement and Admin Display")
print("="*70)

# Create another test client with different details
client2, created = Client.objects.get_or_create(
    email='rajesh.kumar@industries.com',
    defaults={
        'name': 'Rajesh Kumar',
        'company': 'Railway Fabrication Ltd',
        'phone': '+91-9988776655',
        'address': '456 Railway Industrial Zone, Bangalore',
        'industry': 'railway'
    }
)

print(f"\n✓ Customer Information:")
print(f"  Name: {client2.name}")
print(f"  Company: {client2.company}")
print(f"  Email: {client2.email}")
print(f"  Phone: {client2.phone}")
print(f"  Industry: {client2.industry}")

# Get product
product = Product.objects.get(id=12)  # NON AC DOOR ASSEMBLY
print(f"\n✓ Product Details:")
print(f"  Product: {product.name}")
print(f"  Category: {product.category}")
print(f"  Material: {product.material}")

# Create quote request (simulating form submission)
quote2 = QuoteRequest.objects.create(
    client=client2,
    product=product,
    width=600,
    height=900,
    material='aluminium',
    finish='mirror',
    quantity=10,
    special_requirements='High quality finish required. Delivery to Bangalore warehouse.',
    status='pending'
)

print(f"\n✓ Order Successfully Placed!")
print(f"\n  Order ID: {quote2.id}")
print(f"  Dimensions: {quote2.width}mm x {quote2.height}mm")
print(f"  Quantity: {quote2.quantity}")
print(f"  Material: {quote2.material}")
print(f"  Finish: {quote2.finish}")
print(f"  Special Requirements: {quote2.special_requirements}")
print(f"  Status: {quote2.status}")
print(f"  Created: {quote2.created_at}")

# Show all orders
print("\n" + "="*70)
print(" ALL ORDERS IN SYSTEM")
print("="*70)
all_quotes = QuoteRequest.objects.all().select_related('client', 'product')
for i, q in enumerate(all_quotes, 1):
    print(f"\n{i}. Order ID: {q.id}")
    print(f"   Customer: {q.client.name} ({q.client.company})")
    print(f"   Email: {q.client.email}")
    print(f"   Product: {q.product.name}")
    print(f"   Quantity: {q.quantity} units")
    print(f"   Dimensions: {q.width}mm x {q.height}mm")
    print(f"   Material: {q.material}")
    print(f"   Finish: {q.finish}")
    print(f"   Status: {q.status}")
    print(f"   Date: {q.created_at.strftime('%d-%m-%Y %H:%M')}")

print("\n" + "="*70)
print(" ACCESS ADMIN PANEL")
print("="*70)
print("\nURL: http://localhost:8000/admin/pro/quoterequest/")
print("\nYou can now:")
print("  ✓ See all customer orders with their details")
print("  ✓ Filter by status, material, date, or product")
print("  ✓ Search by customer name or email")
print("  ✓ Update order status")
print("  ✓ Add quotes/pricing")
print("="*70)
