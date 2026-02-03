# 📋 Deployment & Setup Checklist

## Phase 1: Pre-Implementation ✅

- [x] Quote Request model exists (pro/models.py)
- [x] Quote Request admin interface available
- [x] Product, Client models configured
- [x] Django admin accessible

---

## Phase 2: Email System Configuration

### 2.1 Gmail Setup
- [ ] Gmail account access (ksree3104@gmail.com)
- [ ] 2-Step Verification enabled on Gmail
  - Go to: https://myaccount.google.com/security
  - Enable 2-Step Verification if not already done
- [ ] Generate App Password
  - In Gmail: Go to App passwords
  - Select: Mail
  - Select: Windows Computer
  - **Save the 16-character password**

### 2.2 Django Settings Update
- [ ] Open `sree/settings.py`
- [ ] Find the EMAIL_HOST_PASSWORD line (~137)
- [ ] Replace `'your_app_password_here'` with your actual 16-character app password
- [ ] Verify EMAIL_HOST_USER is set to `'ksree3104@gmail.com'`
- [ ] Verify ADMIN_EMAIL is set to `'ksree3104@gmail.com'`

**Settings Check:**
```python
# Line ~131-137 in sree/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ksree3104@gmail.com'           ✓
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'       ✓ (16-char app password)
DEFAULT_FROM_EMAIL = 'ksree3104@gmail.com'        ✓
ADMIN_EMAIL = 'ksree3104@gmail.com'              ✓
```

---

## Phase 3: Code Implementation Verification

### 3.1 Check All Required Files Exist
- [x] `pro/signals.py` - Auto email on quote creation
- [x] `pro/email_utils.py` - Email utility functions
- [x] `pro/apps.py` - Signal registration
- [x] `pro/views.py` - Updated with email calls

### 3.2 Verify Code Changes
- [x] `pro/apps.py` has signal import in ready() method
- [x] `pro/views.py` imports email utility functions
- [x] `pro/views.py` calls email functions in views
- [x] `sree/settings.py` has email configuration

---

## Phase 4: Testing

### 4.1 Unit Testing
- [ ] Start Django development server
  ```bash
  python manage.py runserver
  ```

- [ ] Test email configuration (via Django Shell)
  ```bash
  python manage.py shell
  
  from django.core.mail import send_mail
  from django.conf import settings
  
  result = send_mail(
      'Test Subject',
      'Test Message',
      settings.DEFAULT_FROM_EMAIL,
      ['ksree3104@gmail.com']
  )
  print(f"Email sent: {result}")  # Should print: Email sent: 1
  ```

- [ ] Check ksree3104@gmail.com inbox for test email

### 4.2 Feature Testing - Quote Request Form
- [ ] Navigate to: `http://localhost:8000/request-quote/`
- [ ] Fill form with test data:
  - Select existing client or enter new client info
  - Select product
  - Enter width (mm)
  - Enter height (mm)
  - Select material
  - Select finish
  - Enter quantity
  - Add special requirements (optional)
- [ ] Click "Submit"
- [ ] Should see success message: "Quote request submitted successfully!"

### 4.3 Email Verification
After submitting test quote request:
- [ ] Admin email received at ksree3104@gmail.com
  - Contains: Client info, product details, specifications
  - Has: Link to Django admin
  - Format: HTML + Plain text
- [ ] Client email received at submitted email
  - Contains: Confirmation message, quote ID
  - Thanks client for submission
  - States 24-hour response time

### 4.4 Django Admin Verification
- [ ] Login to Django admin: `http://localhost:8000/admin`
- [ ] Navigate to: Admin → Pro → Quote requests
- [ ] Verify submitted quote appears in list
- [ ] Click on quote to view details
- [ ] Verify all information is correctly saved:
  - [ ] Client information
  - [ ] Product selection
  - [ ] Dimensions (width, height)
  - [ ] Material and finish
  - [ ] Quantity
  - [ ] Special requirements
  - [ ] Status (should be "Pending")
  - [ ] Creation date

### 4.5 Admin Features Testing
- [ ] Filter by status
  - [ ] Select "Pending" - see test quote
  - [ ] Select "Quoted" - should be empty
  - [ ] Try other statuses
- [ ] Filter by material
  - Select different materials to verify filter works
- [ ] Filter by creation date
  - Filter for today's date
  - Verify test quote appears
- [ ] Search functionality
  - [ ] Search by client name
  - [ ] Search by product name
- [ ] Update quote status
  - [ ] Change from "Pending" to "Quoted"
  - [ ] Verify update saves
  - [ ] Change back to "Pending"

### 4.6 Contact Form Testing
- [ ] Navigate to: `http://localhost:8000/contact/`
- [ ] Fill in contact form
- [ ] Submit
- [ ] Verify:
  - [ ] Success message shown
  - [ ] Contact saved in Django admin
  - [ ] Confirmation email sent to submitter

---

## Phase 5: Error Handling

### 5.1 Common Issues & Solutions

**Issue: SMTPAuthenticationError**
- [ ] Verify you're using App Password (16 chars), not regular Gmail password
- [ ] Verify EMAIL_HOST_USER matches your Gmail email
- [ ] Verify EMAIL_HOST_PASSWORD is correctly pasted (no extra spaces)

**Issue: Emails go to Spam**
- [ ] Add sender email to Gmail contacts
- [ ] Create filter in Gmail to mark as "Not Spam"

**Issue: Connection Timeout**
- [ ] Check internet connection
- [ ] Check if port 587 is open (firewall)
- [ ] Verify EMAIL_HOST = 'smtp.gmail.com'

**Issue: Emails not sending (silent fail)**
- [ ] Check Django console for error messages
- [ ] Verify email configuration is correct
- [ ] Test with Django shell email send command

---

## Phase 6: Documentation Review

- [ ] Read `QUICK_SETUP.md` - Quick reference guide
- [ ] Read `EMAIL_SETUP.md` - Detailed setup guide
- [ ] Read `QUOTE_REQUEST_SYSTEM.md` - Feature overview
- [ ] Read `SYSTEM_ARCHITECTURE.md` - Technical architecture
- [ ] All documentation is clear and accurate

---

## Phase 7: Security Review

### 7.1 Credentials Management
- [ ] Email credentials NOT hardcoded in production
- [ ] Plan to move to environment variables for production
- [ ] `.env` file will be added to `.gitignore`
- [ ] No credentials in version control

### 7.2 Django Settings
- [ ] EMAIL_BACKEND set to SMTP (not console)
- [ ] EMAIL_USE_TLS = True (secure connection)
- [ ] EMAIL_PORT = 587 (standard TLS port)

### 7.3 Database
- [ ] SQLite used for development (suitable)
- [ ] Plan migration to PostgreSQL for production
- [ ] Regular database backups scheduled (future)

---

## Phase 8: Performance Optimization (Optional)

- [ ] Consider async email sending for production
  - Package: `celery` with Redis/RabbitMQ
- [ ] Email templates optimization
- [ ] Rate limiting on forms (future)
- [ ] Email logging/history (future)

---

## Phase 9: Production Deployment Preparation

### 9.1 Before Going Live
- [ ] Update DEBUG = False in settings.py
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up proper email credentials (use environment variables)
- [ ] Use production database (PostgreSQL)
- [ ] Enable HTTPS/SSL
- [ ] Set up email backup system

### 9.2 Environment Variables Setup (for Production)
```bash
# Create .env file
EMAIL_HOST_USER=ksree3104@gmail.com
EMAIL_HOST_PASSWORD=xxxx_xxxx_xxxx_xxxx
ADMIN_EMAIL=ksree3104@gmail.com

# Install dependency
pip install python-dotenv

# Update settings.py to use os.getenv()
```

### 9.3 Production Deployment Checklist
- [ ] SSL certificate configured
- [ ] Django DEBUG = False
- [ ] ALLOWED_HOSTS configured
- [ ] Secret key rotated
- [ ] Email credentials from environment
- [ ] Database backed up
- [ ] Static files collected
- [ ] Monitoring setup

---

## Phase 10: Post-Deployment

### 10.1 Monitoring
- [ ] Email delivery logs reviewed
- [ ] Django error logs monitored
- [ ] Admin dashboard functional
- [ ] Forms processing correctly

### 10.2 User Communication
- [ ] Users informed about new quote system
- [ ] Support email setup for queries
- [ ] Expected response time communicated (24 hours)

### 10.3 Continuous Improvement
- [ ] Gather user feedback
- [ ] Monitor email delivery rates
- [ ] Optimize email templates based on feedback
- [ ] Plan for email template A/B testing

---

## Sign-Off Checklist

- [ ] All implementations complete
- [ ] All tests passed
- [ ] Documentation reviewed
- [ ] Security check complete
- [ ] Performance acceptable
- [ ] Ready for production

---

## Quick Reference: What Was Added

### Files Created:
```
✓ pro/signals.py           (38 lines) - Email on quote creation
✓ pro/email_utils.py       (99 lines) - Email utility functions
✓ QUICK_SETUP.md           (Quick reference guide)
✓ EMAIL_SETUP.md           (Detailed setup guide)
✓ QUOTE_REQUEST_SYSTEM.md  (Feature overview)
✓ SYSTEM_ARCHITECTURE.md   (Technical diagrams)
```

### Files Modified:
```
✓ sree/settings.py         (+13 lines) - Email configuration
✓ pro/apps.py              (+3 lines)  - Signal registration
✓ pro/views.py             (+7 lines)  - Email function calls
```

### Total Implementation:
- **4 new files created**
- **3 files modified**
- **~180 lines of new code**
- **Email system fully integrated**
- **Quote management complete**

---

**Last Updated:** January 8, 2026  
**Implementation Status:** ✅ COMPLETE  
**Ready for Testing:** YES  
**Ready for Production:** After Phase 7 & 9 completed

---

## Support & Questions

For issues or questions:
1. Check `EMAIL_SETUP.md` for troubleshooting
2. Review `SYSTEM_ARCHITECTURE.md` for understanding flow
3. Check Django console for error messages
4. Verify Gmail account settings
5. Test with Django shell email command

Good luck! 🚀
