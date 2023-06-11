from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from orders.models import Order
from django.http import JsonResponse

# Create your views here.


class OrderAPIView(APIView):
    def post(self,request):
        serializer = OrderSerializer(data= request.data)
        if serializer.is_valid():
            order = Order.objects.create(
                    email=request.data['email'],
                    first_name=request.data['first_name'],
                    last_name=request.data['last_name'],
                    city=request.data['city'],
                    address=serializer.validated_data['address'],
                    PhoneNumber=request.data['PhoneNumber'],
                    vendor=serializer.validated_data['vendor'],
                    product=serializer.validated_data['product'],
                    category=serializer.validated_data['category'],
                )
            if order:
                return Response("Order Created Successfully", status = status.HTTP_200_OK)
            else:
                return Response("Error Creating Order", status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Serializer Not Valid, Check Your Data Inputs", status = status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        all = Order.objects.all()
        serializer = OrderSerializer(all, many = True)
        return JsonResponse({"Orders": serializer.data}, safe=False)