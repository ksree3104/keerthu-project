"""
Email utility functions for Srinivasa Enterprises
"""
from django.core.mail import send_mail
from django.conf import settings


def send_quote_confirmation_email(client_email, client_name, product_name, quote_id):
    """
    Send confirmation email to the client after quote request submission.
    """
    try:
        subject = "Your Quote Request Has Been Received - Srinivasa Enterprises"
        
        message = f"""
        Dear {client_name},
        
        Thank you for submitting your quote request!
        
        We have received your request for {product_name} and our team will review it shortly.
        Your quote request ID is: {quote_id}
        
        We will get back to you within 24 hours with a detailed quote and pricing information.
        
        If you have any questions in the meantime, please feel free to contact us.
        
        Best regards,
        Srinivasa Enterprises Team
        """
        
        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px;">
                        Quote Request Confirmation
                    </h2>
                    
                    <p>Dear <strong>{client_name}</strong>,</p>
                    
                    <p>Thank you for submitting your quote request!</p>
                    
                    <div style="background-color: #ecf0f1; padding: 15px; border-radius: 5px; margin: 20px 0;">
                        <p><strong>Product:</strong> {product_name}</p>
                        <p><strong>Quote Request ID:</strong> {quote_id}</p>
                    </div>
                    
                    <p>Our team will review your request and get back to you within <strong>24 hours</strong> with a detailed quote and pricing information.</p>
                    
                    <p>If you have any questions in the meantime, please feel free to contact us:</p>
                    <ul>
                        <li>Email: {settings.ADMIN_EMAIL}</li>
                        <li>Phone: [Your Company Phone Number]</li>
                    </ul>
                    
                    <p style="margin-top: 30px; border-top: 1px solid #bdc3c7; padding-top: 15px;">
                        Best regards,<br>
                        <strong>Srinivasa Enterprises Team</strong>
                    </p>
                </div>
            </body>
        </html>
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[client_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending confirmation email: {str(e)}")
        return False


def send_contact_confirmation_email(client_email, client_name):
    """
    Send confirmation email to the client after contact form submission.
    """
    try:
        subject = "We've Received Your Contact Information - Srinivasa Enterprises"
        
        message = f"""
        Dear {client_name},
        
        Thank you for getting in touch with us!
        
        We have received your contact information and our team will reach out to you shortly.
        
        We appreciate your interest in Srinivasa Enterprises.
        
        Best regards,
        Srinivasa Enterprises Team
        """
        
        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px;">
                        Contact Confirmation
                    </h2>
                    
                    <p>Dear <strong>{client_name}</strong>,</p>
                    
                    <p>Thank you for getting in touch with us!</p>
                    
                    <p>We have received your contact information and our team will reach out to you shortly to discuss your requirements.</p>
                    
                    <p>We appreciate your interest in Srinivasa Enterprises and look forward to working with you.</p>
                    
                    <p style="margin-top: 30px; border-top: 1px solid #bdc3c7; padding-top: 15px;">
                        Best regards,<br>
                        <strong>Srinivasa Enterprises Team</strong>
                    </p>
                </div>
            </body>
        </html>
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[client_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending contact confirmation email: {str(e)}")
        return False
