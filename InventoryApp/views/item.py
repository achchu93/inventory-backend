from rest_framework import viewsets

from InventoryApp.models import Item
from InventoryApp.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
