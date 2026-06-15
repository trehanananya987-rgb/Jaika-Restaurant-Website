from django.urls import path
from restapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('menu.html', menu, name='menu'),
    path('order.html', order, name='order'),
    path('reserve.html', reserve, name='reserve'),
    path('about.html', about, name='about'),
    path('contact.html',contact, name='contact'),  # use view function, not model
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/show_contact.html', show_contact, name='show_contact'),
    path('dashboard/show_order.html', show_order, name='show_order'),
    path('dashboard/show_reserve.html', show_reserve, name='show_reserve'),
]
