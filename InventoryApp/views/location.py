from rest_framework import viewsets, filters

from InventoryApp.models import Location
from InventoryApp.serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name', 'email', 'address']

	def update(self, request, *args, **kwargs):
		return super().update(request, *args, {**kwargs, 'partial': True})
