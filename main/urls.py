from django.contrib import admin
from django.urls import path, include
from .views import ProductsView

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<int:pk>', ProductsView.as_view())
]
