from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from InventoryApp.models import Vendor, VendorItem, Item
from InventoryApp.serializers import VendorSerializer, OrderSerializer, VendorItemSerializer

class VendorViewSet(viewsets.ModelViewSet):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer

	@action(detail=True, methods=['get'])
	def orders(self, request, pk=None):
		vendor = self.get_object()
		return Response(OrderSerializer(vendor.order_set.all(), many=True).data)

	@action(detail=True, methods=['get', 'post'])
	def items(self, request, pk=None):

		vendor = self.get_object()

		if request.method == 'POST':
			items = request.data.get('items')

			VendorItem.objects.filter(vendor=vendor).delete()

			for item_data in items:
				VendorItem.objects.create(vendor=vendor, item=Item(item_data))

		return Response( VendorItemSerializer(VendorItem.objects.filter(vendor=vendor), many=True).data )

		# try:
		# 	location = request.query_params.get('location')
		# 	print(location)
		# 	vendor = self.get_object()
		# 	unique_items = vendor.order_set.order_by().values_list('items__id', flat=True).distinct()
		# 	report = InventoryReport.objects.filter(inventoryreportitem__item__in=unique_items, closed_at__isnull=False) \
		# 									.prefetch_related('items')

		# 	if not location == None:
		# 		report = report.filter(location=location)

		# 	return Response(InventoryReportSerializer(report.latest('id'))['items'].value)

		# except (NotFound, InventoryReport.DoesNotExist):
		# 	return Response([])
