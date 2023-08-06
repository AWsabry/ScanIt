from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categories_and_products.models import Product
from .serializers import OrderSerializer
from orders.models import Order
from django.http import JsonResponse

# Create your views here.


class OrderAPIView(APIView):
    def post(self, request):
        try:
            product = Product.objects.get(id=request.data['product'])
        except Product.DoesNotExist:
            return Response("Product does not exist.", status=status.HTTP_404_NOT_FOUND)

        vendor = product.vendor

        order = Order.objects.create(
            email=request.data['email'],
            PhoneNumber=request.data['PhoneNumber'],
            product=product,
            vendor=vendor,
        )

        if order:
            return Response("Order Created Successfully", status=status.HTTP_200_OK)
        else:
            return Response("Error Creating Order", status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        all = Order.objects.all()
        serializer = OrderSerializer(all, many = True)
        return JsonResponse({"Orders": serializer.data}, safe=False)