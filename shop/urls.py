from django.urls import path
from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('check/', views.check, name="check"),

]
