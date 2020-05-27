from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    details = serializers.CharField(max_length=100)
    link_img = serializers.ImageField(max_length=None, use_url=True)
