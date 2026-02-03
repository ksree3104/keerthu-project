from django.contrib import admin
from .models import Product, Client, QuoteRequest, FabricationProcess, MaterialAdvisor

def mark_as_completed(modeladmin, request, queryset):
    """Action to mark selected orders as completed"""
    updated = queryset.update(status='completed')
    modeladmin.message_user(request, f'{updated} order(s) marked as completed.')
mark_as_completed.short_description = "Mark selected orders as completed"

def mark_as_pending(modeladmin, request, queryset):
    """Action to mark selected orders as pending"""
    updated = queryset.update(status='pending')
    modeladmin.message_user(request, f'{updated} order(s) marked as pending.')
mark_as_pending.short_description = "Mark selected orders as pending"

def mark_as_quoted(modeladmin, request, queryset):
    """Action to mark selected orders as quoted"""
    updated = queryset.update(status='quoted')
    modeladmin.message_user(request, f'{updated} order(s) marked as quoted.')
mark_as_quoted.short_description = "Mark selected orders as quoted"

def mark_as_approved(modeladmin, request, queryset):
    """Action to mark selected orders as approved"""
    updated = queryset.update(status='approved')
    modeladmin.message_user(request, f'{updated} order(s) marked as approved.')
mark_as_approved.short_description = "Mark selected orders as approved"

def remove_orders(modeladmin, request, queryset):
    """Action to delete selected orders"""
    count = queryset.count()
    queryset.delete()
    modeladmin.message_user(request, f'{count} order(s) removed successfully.')
remove_orders.short_description = "Remove selected orders"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'material', 'category', 'base_price']
    list_filter = ['material', 'category']
    search_fields = ['name', 'description']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'email', 'phone', 'industry', 'created_at']
    list_filter = ['industry', 'created_at']
    search_fields = ['name', 'company', 'email', 'phone']
    readonly_fields = ['created_at']

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'product', 'material', 'quantity', 'status', 'estimated_price', 'created_at']
    list_filter = ['status', 'material', 'created_at', 'product']
    list_editable = ['status']  # Allow inline status editing
    search_fields = ['client__name', 'client__email', 'product__name']
    readonly_fields = ['created_at', 'updated_at', 'id']
    actions = [mark_as_completed, mark_as_approved, mark_as_quoted, mark_as_pending, remove_orders]  # Add bulk actions
    fieldsets = (
        ('Order Information', {
            'fields': ('id', 'created_at', 'updated_at', 'status')
        }),
        ('Client Details', {
            'fields': ('client',)
        }),
        ('Product & Specifications', {
            'fields': ('product', 'material', 'finish', 'width', 'height', 'quantity')
        }),
        ('Additional Info', {
            'fields': ('special_requirements', 'estimated_price')
        }),
    )
    
    def client_name(self, obj):
        return f"{obj.client.name} ({obj.client.company})" if obj.client else "N/A"
    client_name.short_description = 'Client'
    
    def has_delete_permission(self, request, obj=None):
        return True  # Allow deletion through custom action

@admin.register(FabricationProcess)
class FabricationProcessAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_minutes', 'cost_per_unit', 'quality_score']

@admin.register(MaterialAdvisor)
class MaterialAdvisorAdmin(admin.ModelAdmin):
    list_display = ['environment', 'recommended_material']
    list_filter = ['environment', 'recommended_material']
