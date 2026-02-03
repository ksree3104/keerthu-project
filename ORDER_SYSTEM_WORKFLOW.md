# Order System - Complete Workflow Reference

## 🎯 End-to-End Order Processing Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                          CUSTOMER SIDE                               │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────────┐
    │  1. Customer Visits: /request-quote/                │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  2. Form Page Displays with Fields:                  │
    │     ├─ Full Name *                                   │
    │     ├─ Company Name *                                │
    │     ├─ Email *                                       │
    │     ├─ Phone Number *                                │
    │     ├─ Address                                       │
    │     ├─ Industry Type                                 │
    │     ├─ Product Type *                                │
    │     ├─ Material *                                    │
    │     ├─ Width (mm) *                                  │
    │     ├─ Height (mm) *                                 │
    │     ├─ Quantity *                                    │
    │     ├─ Finish *                                      │
    │     └─ Special Requirements                          │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  3. Customer Fills in All Details                    │
    │     ├─ Provides personal information                 │
    │     ├─ Selects product and specifications            │
    │     ├─ Specifies dimensions and quantity             │
    │     └─ Adds any special notes                        │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  4. Customer Clicks "Submit Quote Request"           │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│                       BACKEND PROCESSING                             │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────────┐
    │  5. Django Validates Form:                           │
    │     ├─ Email format check                            │
    │     ├─ Required fields verification                  │
    │     ├─ Product exists validation                     │
    │     └─ Dimensions & quantity check                   │
    └──────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
              ✓ VALID              ✗ INVALID
                    │                   │
                    ▼                   ▼
        ┌──────────────────┐   ┌──────────────────┐
        │  Proceed         │   │  Show Error      │
        └──────────────────┘   │  Messages        │
                │               └──────────────────┘
                │
                ▼
    ┌──────────────────────────────────────────────────────┐
    │  6. Check/Create Customer:                           │
    │     IF email exists in database:                     │
    │        └─ Use existing customer                      │
    │     ELSE:                                            │
    │        └─ Create new customer with:                  │
    │           ├─ Name                                    │
    │           ├─ Company                                 │
    │           ├─ Email                                   │
    │           ├─ Phone                                   │
    │           ├─ Address                                 │
    │           └─ Industry                                │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  7. Create Order in Database:                        │
    │     ├─ Link to customer                              │
    │     ├─ Link to product                               │
    │     ├─ Save specifications:                          │
    │     │   ├─ Width, Height                             │
    │     │   ├─ Material, Finish                          │
    │     │   ├─ Quantity                                  │
    │     │   └─ Special requirements                      │
    │     ├─ Set status to "Pending"                       │
    │     ├─ Record creation timestamp                     │
    │     └─ Assign Order ID                               │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  8. Send Confirmation Email:                         │
    │     ├─ To: customer email                            │
    │     ├─ Subject: Order Confirmation                   │
    │     ├─ Contains:                                     │
    │     │   ├─ Order ID                                  │
    │     │   ├─ Customer name                             │
    │     │   ├─ Product details                           │
    │     │   ├─ Specifications                            │
    │     │   └─ Contact information                       │
    │     └─ Note: Email error doesn't prevent order save  │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼

┌─────────────────────────────────────────────────────────────────────┐
│                        CUSTOMER FEEDBACK                             │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────────┐
    │  9. Display Success Message:                         │
    │                                                       │
    │  "Order placed successfully!                         │
    │   We will contact you within 24 hours with a        │
    │   detailed quote."                                  │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  10. Customer Receives Confirmation Email            │
    │      ├─ Order details                                │
    │      ├─ Contact information                          │
    │      └─ What to expect next                          │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  11. Customer Redirected to Home Page                │
    └──────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────┐
│                          ADMIN SIDE                                  │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────────┐
    │  12. Admin Logs In: /admin/                          │
    │      (Username & Password)                           │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  13. Navigate to Quote Requests:                     │
    │      /admin/pro/quoterequest/                        │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  14. Admin Sees Order List with Columns:             │
    │      ├─ Order ID          #5                         │
    │      ├─ Customer          Vikram Desai               │
    │      │                    (Desai Precision Eng.)     │
    │      ├─ Product           AC - Door Assembly         │
    │      ├─ Material          Stainless Steel            │
    │      ├─ Qty               15 units                   │
    │      ├─ Status            Pending                    │
    │      ├─ Price             -                          │
    │      └─ Date              19-01-2026 04:14:57        │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  15. Admin Can:                                      │
    │      ├─ SEARCH:                                      │
    │      │   ├─ By customer name (Vikram)                │
    │      │   ├─ By email (vikram.desai@...)              │
    │      │   └─ By product (Door Assembly)               │
    │      ├─ FILTER:                                      │
    │      │   ├─ By status (Pending, Quoted, etc.)        │
    │      │   ├─ By material (Stainless, Aluminium)       │
    │      │   ├─ By date (Today, This week, etc.)         │
    │      │   └─ By product type                          │
    │      ├─ VIEW DETAILS:                                │
    │      │   ├─ Full customer information                │
    │      │   ├─ Complete order specifications            │
    │      │   ├─ Special requirements                     │
    │      │   └─ Status history                           │
    │      ├─ EDIT:                                        │
    │      │   ├─ Update status (Pending→Quoted)           │
    │      │   ├─ Add estimated price                      │
    │      │   ├─ Add special notes                        │
    │      │   └─ Save changes                             │
    │      └─ PROTECT:                                     │
    │          ├─ Cannot delete orders (protected)         │
    │          └─ Ensures data safety                      │
    └──────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌──────────────────────────────────────────────────────┐
    │  16. Admin Actions:                                  │
    │      1. Review order details                         │
    │      2. Calculate quote based on specifications      │
    │      3. Update status to "Quoted"                    │
    │      4. Enter estimated price                        │
    │      5. Add processing notes                         │
    │      6. Save changes                                 │
    │      7. Send quote to customer via email             │
    │      8. Track order progress                         │
    └──────────────────────────────────────────────────────┘
```

---

## 📊 Database Schema

```
┌─────────────────────────┐
│    CLIENT TABLE         │
├─────────────────────────┤
│ id (PK)                 │
│ name                    │
│ company                 │
│ email (UNIQUE)          │
│ phone                   │
│ address                 │
│ industry                │
│ created_at              │
└─────────────────────────┘
         │
         │ (1 to Many)
         │
         ▼
┌─────────────────────────┐
│  QUOTEREQUEST TABLE     │
├─────────────────────────┤
│ id (PK)                 │
│ client_id (FK)          │
│ product_id (FK)         │
│ width                   │
│ height                  │
│ material                │
│ finish                  │
│ quantity                │
│ special_requirements    │
│ estimated_price         │
│ status                  │
│ created_at              │
│ updated_at              │
└─────────────────────────┘
         │
         │ (Many to 1)
         │
         ▼
┌─────────────────────────┐
│   PRODUCT TABLE         │
├─────────────────────────┤
│ id (PK)                 │
│ name                    │
│ description             │
│ material                │
│ category                │
│ image                   │
│ base_price              │
│ created_at              │
└─────────────────────────┘
```

---

## 🔄 Status Flow

```
Customer places order
        │
        ▼
    [PENDING]  ◄─── Initial status when order is placed
        │
        │ (Admin reviews and calculates quote)
        │
        ▼
    [QUOTED]   ◄─── Price quote has been provided to customer
        │
        │ (Customer accepts the quote)
        │
        ▼
    [APPROVED] ◄─── Customer has approved and order is active
        │
        │ (Work in progress)
        │
        ▼
    [COMPLETED] ◄─── Order has been completed and delivered
        │
        or
        │
        ▼
    [REJECTED]  ◄─── Order was not approved by customer
```

---

## ✅ Verification Checklist

✓ **Form Fields**: All customer and product information collected
✓ **Validation**: Email format and required fields validated
✓ **Database**: Orders saved correctly with all details
✓ **Customer Email**: Confirmation sent (if configured)
✓ **Success Message**: Displayed after order placement
✓ **Admin Display**: All orders visible in admin panel
✓ **Search**: Works by customer name, email, product
✓ **Filters**: Works by status, material, date, product
✓ **Data Protection**: Orders can't be accidentally deleted
✓ **Error Handling**: Gracefully handles errors
✓ **No Errors**: Django checks pass cleanly

---

**System Status**: ✅ PRODUCTION READY
**Last Updated**: 19-01-2026
**Version**: 1.0
