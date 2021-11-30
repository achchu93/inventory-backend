from rest_framework import viewsets

from InventoryApp.models import Receipt
from InventoryApp.serializers import ReceiptSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer
