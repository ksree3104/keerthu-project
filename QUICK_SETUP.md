# 🚀 Quick Start - Email & Quote Request System

## ⚡ 30-Second Setup

### Step 1: Get Gmail App Password
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Click "App passwords" 
3. Select "Mail" and "Windows Computer"
4. Copy the 16-character password

### Step 2: Update Django Settings
Edit `sree/settings.py` (line ~137):
```python
EMAIL_HOST_PASSWORD = 'paste_your_16_character_password_here'
```

### Step 3: Done! 🎉
That's it! Email system is ready.

---

## 📧 What Happens Now?

### When someone submits a Quote Request:
1. ✅ Quote is saved in Django Admin
2. ✅ Email sent to admin: `ksree3104@gmail.com`
3. ✅ Email sent to client with confirmation

### When someone submits Contact Form:
1. ✅ Contact info saved
2. ✅ Email sent to client confirming receipt

---

## 🔍 Where to Find Quotes?

### In Django Admin:
```
URL: http://localhost:8000/admin
Path: Pro > Quote requests
```

### Admin Features:
- Filter by Status (Pending, Quoted, Approved, Rejected, Completed)
- Filter by Material Type
- Filter by Date
- Search by Client Name or Product Name

---

## 📬 Email Recipients

| Event | Recipient | Content |
|-------|-----------|---------|
| New Quote Request | Admin | Full quote details + client info |
| Quote Submitted | Client | Confirmation + Quote ID |
| Contact Form | Client | Thank you message |

---

## ✅ Testing the System

### Quick Test:
1. Navigate to: `http://localhost:8000/request-quote/`
2. Fill out form and submit
3. Check your email for:
   - Admin email (ksree3104@gmail.com) - detailed quote info
   - Your email - confirmation message

### Command Line Test:
```bash
python manage.py shell

# Then run:
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'This is a test',
    settings.DEFAULT_FROM_EMAIL,
    ['ksree3104@gmail.com']
)
# Check your inbox!
```

---

## 🐛 Troubleshooting

### Issue: "SMTPAuthenticationError"
**Solution:** Use Gmail App Password (not regular password)
- Regular password ❌
- 16-character App Password ✅

### Issue: Emails not received
**Solution:** Check settings:
```python
# Make sure this is set correctly:
EMAIL_HOST_PASSWORD = 'your_actual_app_password'
```

### Issue: Emails in Spam folder
**Solution:** Add sender email to contacts in Gmail

### Issue: Still not working?
**Enable Console Email (for testing):**
Edit `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Emails will print to terminal instead. Then switch back to SMTP.

---

## 📁 Important Files

```
pro/
├── signals.py          ← Auto email when quote created
├── email_utils.py      ← Email functions
├── views.py            ← Updated with email calls
└── admin.py            ← Quote management dashboard

sree/
└── settings.py         ← Email configuration
```

---

## 🔐 Security Reminder

✅ Use App Password (not account password)
✅ Never share or commit credentials to git
✅ For production, use environment variables

---

## 📊 Admin Dashboard Features

### Quote Request Management:
- View all quotes in one place
- Update quote status
- Filter and search quotes
- View complete client information
- See all quote specifications
- Track creation and modification dates

### Statuses Available:
- 🟡 Pending - New quotes awaiting review
- 🔵 Quoted - Price estimate provided
- 🟢 Approved - Client approved the quote
- 🔴 Rejected - Quote rejected
- ⚪ Completed - Order fulfilled

---

## 🎯 Next Steps

1. ✅ Get Gmail App Password
2. ✅ Update EMAIL_HOST_PASSWORD in settings.py
3. ✅ Test the system with a quote request
4. ✅ Monitor Django Admin for incoming quotes
5. ✅ Update quote status as you process them
6. ✅ Clients receive confirmation emails

---

**Ready to use! Start receiving quote requests with automatic email notifications. 🚀**

For detailed information, see `EMAIL_SETUP.md` or `QUOTE_REQUEST_SYSTEM.md`
