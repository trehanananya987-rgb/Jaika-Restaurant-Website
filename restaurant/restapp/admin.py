from django.contrib import admin
from .models import Contact, Order, Reserve

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'select_dish', 'quantity')

@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'date', 'time', 'number_of_guest')
