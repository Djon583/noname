from django.contrib import admin
from .models import Products, Category, ListOrders, Comments

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(ListOrders)
admin.site.register(Comments)
