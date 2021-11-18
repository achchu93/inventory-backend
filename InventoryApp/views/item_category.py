from rest_framework import viewsets

from InventoryApp.models import ItemCategory
from InventoryApp.serializers import ItemCategorySerializer

class ItemCategoryViewSet(viewsets.ModelViewSet):
	queryset = ItemCategory.objects.all()
	serializer_class = ItemCategorySerializer
