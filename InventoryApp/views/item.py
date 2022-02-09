from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from InventoryApp.models import Item, VendorItem, Vendor, Order
from InventoryApp.serializers import ItemSerializer, ItemVendorsSerializer, OrderSerializer

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	@action(detail=True, methods=['get', 'post'])
	def vendors(self, request, pk=None):
		item = self.get_object()

		if request.method == 'POST':
			vendors = request.data.get('vendors')

			VendorItem.objects.filter(item=item).delete()

			for vendor_data in vendors:
				VendorItem.objects.create(vendor=Vendor(vendor_data), item=item)

		return Response( ItemVendorsSerializer(VendorItem.objects.filter(item=item), many=True).data )

	@action(detail=True, methods=['get'])
	def orders(self, request, pk=None):
		item = self.get_object()

		return Response( OrderSerializer(Order.objects.filter(items__in=[item.id]), many=True).data )
