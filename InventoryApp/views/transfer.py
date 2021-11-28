from rest_framework import viewsets

from InventoryApp.models import Transfer
from InventoryApp.serializers import TransferSerializer

class TransferViewSet(viewsets.ModelViewSet):
	queryset = Transfer.objects.all()
	serializer_class = TransferSerializer
