from rest_framework import viewsets

from InventoryApp.models import Sku
from InventoryApp.serializers import SkuSerializer

class SkuViewSet(viewsets.ModelViewSet):
	queryset = Sku.objects.all()
	serializer_class = SkuSerializer
