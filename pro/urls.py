"""
URL configuration for sree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('expertise/', views.expertise, name='expertise'),
    path('credentials/', views.credentials, name='credentials'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),
    path('contact-new/', views.contact_new, name='contact_new'),
    path('request-quote/', views.request_quote, name='request_quote'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('material-advisor/', views.material_advisor, name='material_advisor'),
]
