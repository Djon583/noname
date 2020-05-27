from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)    
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    details = serializers.CharField(max_length=100)
    link_img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Products
        fields = '__all__'        
