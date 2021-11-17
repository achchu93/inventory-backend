from rest_framework import viewsets

from InventoryApp.models import Vendor
from InventoryApp.serializers import VendorSerializer

class VendorViewSet(viewsets.ModelViewSet):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer
