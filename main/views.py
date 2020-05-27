from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Products
from .serializers import ProductsSerializer

class ProductsView(APIView):
    permission_classes = ()
    def get(self,request, *args, **kwargs):
        products = Products.objects.all()
        result = {}
        for product in products:
            serializer = ProductsSerializer(product, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self,request,*args,**kwargs):
        file_serializer = ProductsSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    """
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({"Products": serializer.data})

    def post(self, request):
        products = request.data.get('')
        serializer = ProductsSerializer(data=products)
        if serializer.is_valid(raise_exception=True):
            products_saved = serializer.save()
        return Response({"success": "Products '{}' created successfully".format(products.title)})
        """
