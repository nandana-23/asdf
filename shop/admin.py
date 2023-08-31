from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(customer)
admin.site.register(product)
admin.site.register(Order)
admin.site.register(orderitem)
admin.site.register(shippingaddress)
