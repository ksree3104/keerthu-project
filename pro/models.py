from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    material = models.CharField(max_length=50, choices=[
        ('aluminium', 'Aluminium'),
        ('stainless', 'Stainless Steel')
    ])
    category = models.CharField(max_length=50, choices=[
        ('door', 'Door Assembly'),
        ('window', 'Lavatory Window'),
        ('panel', 'Panel/Cover'),
        ('loader_arm', 'Loader Arm Assembly'),
        ('cubical_door', 'Cubical Door Assembly')
    ])
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    industry = models.CharField(max_length=100, choices=[
        ('railway', 'Railway'),
        ('automotive', 'Automotive'),
        ('engineering', 'Engineering'),
        ('other', 'Other')
    ], default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"

class QuoteRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='quotes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    width = models.DecimalField(max_digits=6, decimal_places=2, help_text="Width in mm")
    height = models.DecimalField(max_digits=6, decimal_places=2, help_text="Height in mm")
    material = models.CharField(max_length=50, choices=[
        ('aluminium', 'Aluminium'),
        ('stainless', 'Stainless Steel')
    ])
    finish = models.CharField(max_length=50, choices=[
        ('brushed', 'Brushed'),
        ('mirror', 'Mirror'),
        ('bead', 'Bead-blast'),
        ('powder', 'Powder-coat')
    ])
    quantity = models.IntegerField(default=1)
    special_requirements = models.TextField(blank=True)
    estimated_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('quoted', 'Quoted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Quote for {self.product.name} - {self.client.name}"

class FabricationProcess(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time_minutes = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    quality_score = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class MaterialAdvisor(models.Model):
    environment = models.CharField(max_length=50)
    weight_sensitivity = models.CharField(max_length=50)
    budget = models.CharField(max_length=50)
    finish_preference = models.CharField(max_length=50)
    recommended_material = models.CharField(max_length=50)
    reasoning = models.TextField()
    tradeoffs = models.TextField(blank=True)

    def __str__(self):
        return f"Advisor: {self.environment} -> {self.recommended_material}"
