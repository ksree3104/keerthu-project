# System Architecture - Quote Request & Email Flow

## 📊 System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SRINIVASA ENTERPRISES WEBSITE                │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ↓                     ↓                     ↓
   ┌─────────┐          ┌──────────┐          ┌──────────┐
   │ Contact │          │  Quote   │          │ Product  │
   │  Form   │          │ Request  │          │  Detail  │
   │         │          │   Form   │          │          │
   └────┬────┘          └────┬─────┘          └──────────┘
        │                    │
        └────────┬───────────┘
                 │
                 ↓
        ┌─────────────────────────────────────────┐
        │  Django Views & Forms Validation        │
        │  (pro/views.py)                         │
        └────────┬────────────────────────────────┘
                 │
                 ↓
        ┌─────────────────────────────────────────┐
        │  Database Models                        │
        │  - Client                               │
        │  - QuoteRequest                         │
        │  (pro/models.py)                        │
        └────┬────────────────────────────────────┘
             │
    ┌────────┴────────┬──────────────┐
    │                 │              │
    ↓                 ↓              ↓
┌─────────┐    ┌─────────────┐   ┌──────────┐
│ Signal  │    │ Email Utils │   │ Admin    │
│Triggered│    │ Functions   │   │ Backend  │
└────┬────┘    └──────┬──────┘   └─────┬────┘
     │                │                │
     ↓                ↓                ↓
┌──────────────────────────────────────────────────┐
│         Django Email System (SMTP)               │
│  - Backend: SMTP                                 │
│  - Host: smtp.gmail.com                          │
│  - Port: 587 (TLS)                               │
│  - Account: ksree3104@gmail.com                  │
└────────┬──────────────────┬──────────────────────┘
         │                  │
    ┌────┴────┐         ┌────┴─────────┐
    │          │         │              │
    ↓          ↓         ↓              ↓
┌──────────┐ ┌────────┐ ┌────────────┐ ┌──────┐
│   Admin  │ │Client  │ │  Gmail     │ │ Logs │
│  Email   │ │ Email  │ │  Server    │ │      │
│ Notifctn │ │Confirm │ │ Processing │ │      │
└──────────┘ └────────┘ └────────────┘ └──────┘
    │            │            │
    ↓            ↓            ↓
┌──────────────────────────────────────────────────┐
│         Admin Dashboard (Django Admin)           │
│  - View All Quotes                               │
│  - Update Status                                 │
│  - Filter & Search                               │
│  - Client Information                            │
└──────────────────────────────────────────────────┘
    │
    ├─ Pending
    ├─ Quoted
    ├─ Approved
    ├─ Rejected
    └─ Completed
```

---

## 🔄 Quote Request Processing Flow

```
USER SUBMITS QUOTE REQUEST
         │
         ↓
    ┌─────────────────────────────────────────────┐
    │  1. Form Submitted to Server                │
    │     - Client Info: Name, Email, Company    │
    │     - Product: Type, Material, Finish      │
    │     - Specs: Width, Height, Quantity       │
    │     - Special Requirements                 │
    └──────────┬──────────────────────────────────┘
               │
               ↓
    ┌─────────────────────────────────────────────┐
    │  2. Django Validates & Saves                │
    │     - Models: Client, QuoteRequest          │
    │     - Database: SQLite3 (db.sqlite3)        │
    └──────────┬──────────────────────────────────┘
               │
               ↓
    ┌─────────────────────────────────────────────┐
    │  3. Signal Triggered (post_save)            │
    │     - File: pro/signals.py                  │
    │     - Automatically fires                   │
    └──────────┬──────────────────────────────────┘
               │
        ┌──────┴──────┐
        │             │
        ↓             ↓
    ┌────────────┐  ┌─────────────────┐
    │ Email 1:   │  │ Email 2:        │
    │ ADMIN      │  │ CLIENT          │
    │ NOTIF      │  │ CONFIRMATION    │
    └────┬───────┘  └────┬────────────┘
         │                │
         ↓                ↓
    ┌─────────────────────────────────────────────┐
    │  4. SMTP Email Delivery (Gmail)             │
    │     - Host: smtp.gmail.com                  │
    │     - Port: 587                             │
    │     - Account: ksree3104@gmail.com          │
    └──────────┬──────────────────────────────────┘
               │
        ┌──────┴──────┐
        │             │
        ↓             ↓
    ┌────────────┐  ┌─────────────────┐
    │ ADMIN      │  │ CLIENT          │
    │ INBOX      │  │ INBOX           │
    │ (Details)  │  │ (Confirmation)  │
    └────────────┘  └─────────────────┘
        │                │
        ↓                ↓
    ADMIN REVIEWS      CLIENT GETS
    & UPDATES          CONFIRMATION
    QUOTE              & QUOTE ID
```

---

## 📧 Email Content Comparison

### ADMIN EMAIL (Detailed Notification)
```
From: ksree3104@gmail.com
To: ksree3104@gmail.com
Subject: New Quote Request - [Product Name]

Content:
├─ CLIENT INFO
│  ├─ Name
│  ├─ Company
│  ├─ Email & Phone
│  └─ Industry
├─ PRODUCT DETAILS
│  ├─ Product Name
│  ├─ Category
│  ├─ Material
│  └─ Finish
├─ SPECIFICATIONS
│  ├─ Width (mm)
│  ├─ Height (mm)
│  └─ Quantity
└─ ADMIN LINK
   └─ Django Admin URL
```

### CLIENT EMAIL (Confirmation)
```
From: ksree3104@gmail.com
To: [Client Email]
Subject: Your Quote Request Confirmation

Content:
├─ GREETING
│  └─ Hello [Client Name]
├─ CONFIRMATION
│  └─ Thank you message
├─ REFERENCE INFO
│  ├─ Product Name
│  └─ Quote Request ID
└─ EXPECTATION
   └─ Response within 24 hours
```

---

## 🗂️ Database Schema

```
┌─────────────┐
│   Client    │
├─────────────┤
│ id (PK)     │
│ name        │
│ company     │
│ email       │
│ phone       │
│ address     │
│ industry    │
│ created_at  │
└──────┬──────┘
       │
       │ 1:N
       │
       ↓
┌──────────────────┐
│  QuoteRequest    │
├──────────────────┤
│ id (PK)          │
│ client_id (FK)   │────→ CLIENT
│ product_id (FK)  │────→ PRODUCT
│ width            │
│ height           │
│ material         │
│ finish           │
│ quantity         │
│ special_req...   │
│ estimated_price  │
│ status           │
│ created_at       │
│ updated_at       │
└──────────────────┘
       │
       │
       ↓
┌─────────────┐
│  Product    │
├─────────────┤
│ id (PK)     │
│ name        │
│ description │
│ material    │
│ category    │
│ image       │
│ base_price  │
│ created_at  │
└─────────────┘
```

---

## 🔌 Signal & Email Integration

```
Django Signal System (pro/signals.py)
┌────────────────────────────────────────┐
│ @receiver(post_save, sender=QuoteRequest)│
│                                        │
│ When QuoteRequest is saved:           │
│ if created == True:                   │
│    send_mail() to admin               │
│    └─ HTML formatted email            │
│    └─ Plain text email                │
│    └─ Complete details                │
└────────────┬───────────────────────────┘
             │
             ↓
View Function (pro/views.py)
┌────────────────────────────────────────┐
│ def request_quote(request):           │
│    form.save()                        │
│    send_quote_confirmation_email()    │
│    └─ Email to client                 │
│    └─ Thank you message               │
│    └─ Quote ID                        │
│    redirect('home')                   │
└────────────────────────────────────────┘
```

---

## 🚦 Quote Status Workflow

```
                    ┌─────────────┐
                    │  PENDING    │ ← Quote Created
                    │ (Awaiting)  │
                    └──────┬──────┘
                           │
                    ┌──────↓──────┐
                    │   QUOTED    │ ← Price Provided
                    │ (Estimated) │
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │                         │
         ┌────↓────┐             ┌─────↓────┐
         │APPROVED │             │ REJECTED │
         │(Accepted)│             │ (Denied) │
         └────┬─────┘             └──────────┘
              │
         ┌────↓──────┐
         │ COMPLETED │ ← Order Fulfilled
         │(Delivered)│
         └───────────┘
```

---

## 📱 User Journey

```
┌─────────────────────────────────────────────┐
│  USER VISITS WEBSITE                        │
└────────────┬────────────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ↓             ↓
  ┌────────┐   ┌──────────────┐
  │Contact │   │Request Quote │
  │  Form  │   │    Form      │
  └───┬────┘   └──────┬───────┘
      │               │
      ↓               ↓
  ┌──────────────────────────────────────┐
  │  Fill Out Form & Submit              │
  └──────────┬───────────────────────────┘
             │
             ↓
  ┌──────────────────────────────────────┐
  │  Success Message Displayed           │
  │  "Quote submitted successfully!"     │
  └──────────┬───────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ↓             ↓
┌──────────────┐  ┌──────────────────┐
│ User Inbox   │  │ Admin Inbox      │
│              │  │                  │
│ Confirmation │  │ Quote Details    │
│ Email        │  │ Client Info      │
│              │  │ Request Details  │
└──────────────┘  └────────┬─────────┘
                           │
                           ↓
                  ┌──────────────────┐
                  │ Django Admin     │
                  │ Review & Process │
                  │ Update Status    │
                  │ Send Quote       │
                  └──────────────────┘
```

---

**Generated:** January 8, 2026  
**Version:** 1.0  
**Status:** Complete ✅
