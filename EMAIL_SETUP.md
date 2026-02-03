# Email Configuration Guide

## Overview
This Django project now includes automatic email notifications for quote requests. When a quote request is submitted, emails are sent to:
1. **Admin Email** (ksree3104@gmail.com) - Notification of new quote request
2. **Client Email** - Confirmation that their quote request was received

## Setup Instructions

### 1. Gmail App Password Setup (IMPORTANT)

Since the system uses Gmail's SMTP server, you need to set up an **App Password** (not your regular Gmail password):

#### Steps:
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Look for "App passwords" in the left menu
3. If you don't see it, enable 2-Step Verification first
4. Select "Mail" and "Windows Computer"
5. Google will generate a 16-character app password
6. Copy this password

### 2. Update Django Settings

Open `sree/settings.py` and update the email configuration:

```python
EMAIL_HOST_USER = 'ksree3104@gmail.com'
EMAIL_HOST_PASSWORD = 'paste_your_16_char_app_password_here'
ADMIN_EMAIL = 'ksree3104@gmail.com'
```

**Security Note:** In production, use environment variables instead of hardcoding credentials:

```python
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
```

### 3. Email Configuration Summary

The following settings are already configured in `sree/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'ksree3104@gmail.com'
```

### 4. How It Works

#### Signal-Based Email (Automatic)
- **File:** `pro/signals.py`
- **Trigger:** When a new QuoteRequest is created
- **Recipient:** Admin email (ksree3104@gmail.com)
- **Content:** Complete quote request details with client info, product specs, and dimensions

#### Function-Based Emails (Manual)
- **File:** `pro/email_utils.py`
- **Functions:**
  - `send_quote_confirmation_email()` - Sent after quote request submission
  - `send_contact_confirmation_email()` - Sent after contact form submission
- **Called from:** `pro/views.py`

### 5. Admin Dashboard Features

The Quote Request admin interface now includes:
- Filter by status (Pending, Quoted, Approved, Rejected, Completed)
- Filter by material type
- Filter by creation date
- Search by client name or product name
- View all quote details including client information and specifications

### 6. Testing Email Functionality

#### Test Email Sending (Console Backend - Development)

Add this to `settings.py` for testing without actually sending emails:

```python
# For development/testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

#### Manual Test via Django Shell

```bash
python manage.py shell
```

Then run:
```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    subject='Test Email',
    message='This is a test email',
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=['ksree3104@gmail.com'],
)
```

### 7. File Changes Summary

**Modified Files:**
- `sree/settings.py` - Added email configuration
- `pro/apps.py` - Added signal registration
- `pro/views.py` - Added email sending calls

**New Files:**
- `pro/signals.py` - Signal handlers for automatic emails
- `pro/email_utils.py` - Email utility functions

### 8. Current Email Flow

```
User submits Quote Request
        ↓
QuoteRequest object created
        ↓
Signal triggered (signals.py)
        ↓
Email sent to Admin (ksree3104@gmail.com)
        ↓
Email sent to Client (confirmation)
```

### 9. Troubleshooting

#### "SMTPAuthenticationError"
- Check if you're using the correct Gmail App Password (not your regular password)
- Verify EMAIL_HOST_USER matches the Gmail account
- Ensure 2-Step Verification is enabled on your Gmail account

#### Emails not being sent
- Check Django console for error messages
- Verify EMAIL_BACKEND is set correctly
- Ensure your internet connection is working
- Check if Gmail is blocking the connection (less secure app access)

#### Email appears in Spam
- Add your Django sender email to Gmail contacts
- Create a Gmail filter to mark emails as "Not Spam"

### 10. Email Templates

You can customize the email templates in `pro/email_utils.py` and `pro/signals.py` by modifying the `message` and `html_message` variables.

---

**Last Updated:** January 8, 2026
**Status:** Ready for Production
