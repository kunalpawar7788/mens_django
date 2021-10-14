from django.contrib import admin

from .models import Order, OrderItem

# admin.site.register(Order)


class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order)