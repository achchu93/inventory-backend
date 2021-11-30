from rest_framework import viewsets

from InventoryApp.models import ReceiptFile
from InventoryApp.serializers import ReceiptFileSerializer

class ReceiptFileViewSet(viewsets.ModelViewSet):
	queryset = ReceiptFile.objects.all()
	serializer_class = ReceiptFileSerializer
