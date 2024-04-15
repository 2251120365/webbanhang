from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('', views.home, name='home'),
    path('update_item/', views.updateItem, name='update_item'),
    path ('search/', views.search, name="search"),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('customer/', views.customerView, name='customer'),
    # path('category/', views.category, name='category'),
    path('detail/', views.detail, name='detail'),
    path('about-us/', views.aboutUs, name='about_us'),
]

