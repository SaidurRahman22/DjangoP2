from django.contrib import admin
from django.urls import path
from pharma import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index.html", views.index, name='index'),
    path("shop.html", views.shop, name='shop'),
    path("single.html", views.single, name='single'),
    path("cart.html", views.cart, name='cart'),
    path("about.html", views.about, name='about'),
    path("contact.html", views.contact, name='contact'),
    path("checkout.html", views.checkout, name='checkout'),
    path("login.html", views.login, name='login'),
    path("reg.html", views.reg, name='reg'),
]
