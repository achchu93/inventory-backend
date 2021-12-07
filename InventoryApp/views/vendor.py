from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from InventoryApp.models import Vendor, InventoryReport
from InventoryApp.models.order import Order
from InventoryApp.serializers import VendorSerializer, InventoryReportSerializer, OrderSerializer

class VendorViewSet(viewsets.ModelViewSet):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer

	@action(detail=True, methods=['get'])
	def orders(self, request, pk=None):
		vendor = self.get_object()
		return Response(OrderSerializer(vendor.order_set.all(), many=True).data)

	@action(detail=True, methods=['get'])
	def items(self, request, pk=None):

		try:
			location = request.query_params.get('location')
			print(location)
			vendor = self.get_object()
			unique_items = vendor.order_set.order_by().values_list('items__id', flat=True).distinct()
			report = InventoryReport.objects.filter(inventoryreportitem__item__in=unique_items, closed_at__isnull=False) \
											.prefetch_related('items')

			if not location == None:
				report = report.filter(location=location)

			return Response(InventoryReportSerializer(report.latest('id'))['items'].value)

		except (NotFound, InventoryReport.DoesNotExist):
			return Response([])
