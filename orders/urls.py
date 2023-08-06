from django.urls import path
from .views import OrderAPIView


app_name = 'orders'

urlpatterns = [
    
    path('orders/',view=OrderAPIView.as_view(), name= "orders"),
]
