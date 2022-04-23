from rest_framework import viewsets
from django_filters import rest_framework as filters

from InventoryApp.models import Transfer
from InventoryApp.serializers import TransferSerializer
from InventoryApp.filters import TransferFilter

class TransferViewSet(viewsets.ModelViewSet):
	queryset = Transfer.objects.all()
	serializer_class = TransferSerializer
	# filter_backends = (filters.DjangoFilterBackend)
	filterset_class = TransferFilter
