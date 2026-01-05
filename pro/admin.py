from django.contrib import admin
from .models import Product, Client, QuoteRequest, FabricationProcess, MaterialAdvisor

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'category', 'base_price']
    list_filter = ['material', 'category']
    search_fields = ['name', 'description']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'email', 'phone', 'industry']
    list_filter = ['industry']
    search_fields = ['name', 'company', 'email']

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'material', 'status', 'estimated_price', 'created_at']
    list_filter = ['status', 'material', 'created_at']
    search_fields = ['client__name', 'product__name']
    readonly_fields = ['estimated_price', 'created_at', 'updated_at']

@admin.register(FabricationProcess)
class FabricationProcessAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_minutes', 'cost_per_unit', 'quality_score']

@admin.register(MaterialAdvisor)
class MaterialAdvisorAdmin(admin.ModelAdmin):
    list_display = ['environment', 'recommended_material']
    list_filter = ['environment', 'recommended_material']
