from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from InventoryApp.models import Order, Receipt
from InventoryApp.serializers import OrderSerializer, ReceiptSerializer

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	@action(detail=True, methods=['get'])
	def receipts(self, request, pk=None):
		order = self.get_object()

		return Response( ReceiptSerializer( Receipt.objects.filter(order=order), many=True ).data )
