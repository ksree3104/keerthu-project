from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import QuoteRequest

@receiver(post_save, sender=QuoteRequest)
def send_quote_request_email(sender, instance, created, **kwargs):
    """
    Signal handler to send email notifications when a new quote request is created.
    Sends email to admin when a new order/quote request is placed.
    """
    if created:
        try:
            # Prepare email content
            subject = f"New Quote Request - {instance.product.name}"
            
            message = f"""
            A new quote request has been submitted!
            
            ========== QUOTE REQUEST DETAILS ==========
            
            CLIENT INFORMATION:
            Name: {instance.client.name}
            Company: {instance.client.company}
            Email: {instance.client.email}
            Phone: {instance.client.phone}
            Industry: {instance.client.get_industry_display()}
            
            PRODUCT DETAILS:
            Product: {instance.product.name}
            Category: {instance.product.get_category_display()}
            Material: {instance.get_material_display()}
            Finish: {instance.get_finish_display()}
            
            SPECIFICATIONS:
            Width: {instance.width} mm
            Height: {instance.height} mm
            Quantity: {instance.quantity}
            
            SPECIAL REQUIREMENTS:
            {instance.special_requirements if instance.special_requirements else "None"}
            
            ==========================================
            
            Status: {instance.get_status_display()}
            Created Date: {instance.created_at}
            
            Please log in to Django Admin to review and respond to this quote request.
            Admin URL: {settings.SITE_URL if hasattr(settings, 'SITE_URL') else 'http://127.0.0.1:8000'}/admin/pro/quoterequest/
            """
            
            html_message = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <h2 style="color: #2c3e50;">New Quote Request Received!</h2>
                    
                    <h3 style="color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px;">CLIENT INFORMATION</h3>
                    <p><strong>Name:</strong> {instance.client.name}</p>
                    <p><strong>Company:</strong> {instance.client.company}</p>
                    <p><strong>Email:</strong> <a href="mailto:{instance.client.email}">{instance.client.email}</a></p>
                    <p><strong>Phone:</strong> {instance.client.phone}</p>
                    <p><strong>Industry:</strong> {instance.client.get_industry_display()}</p>
                    
                    <h3 style="color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px;">PRODUCT DETAILS</h3>
                    <p><strong>Product:</strong> {instance.product.name}</p>
                    <p><strong>Category:</strong> {instance.product.get_category_display()}</p>
                    <p><strong>Material:</strong> {instance.get_material_display()}</p>
                    <p><strong>Finish:</strong> {instance.get_finish_display()}</p>
                    
                    <h3 style="color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px;">SPECIFICATIONS</h3>
                    <p><strong>Width:</strong> {instance.width} mm</p>
                    <p><strong>Height:</strong> {instance.height} mm</p>
                    <p><strong>Quantity:</strong> {instance.quantity}</p>
                    
                    <h3 style="color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px;">SPECIAL REQUIREMENTS</h3>
                    <p>{instance.special_requirements if instance.special_requirements else 'None'}</p>
                    
                    <p style="margin-top: 30px; padding: 15px; background-color: #ecf0f1; border-radius: 5px;">
                        <strong>Status:</strong> {instance.get_status_display()}<br>
                        <strong>Created:</strong> {instance.created_at}
                    </p>
                </body>
            </html>
            """
            
            # Send email to admin
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                html_message=html_message,
                fail_silently=False,
            )
            
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            # In production, you might want to log this error
