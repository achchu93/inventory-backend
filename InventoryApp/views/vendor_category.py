from rest_framework import viewsets

from InventoryApp.models import VendorCategory
from InventoryApp.serializers import VendorCategorySerializer

class VendorCategoryViewSet(viewsets.ModelViewSet):
	queryset = VendorCategory.objects.all()
	serializer_class = VendorCategorySerializer
