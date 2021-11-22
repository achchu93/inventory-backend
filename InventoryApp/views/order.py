from rest_framework import viewsets

from InventoryApp.models import Order
from InventoryApp.serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
