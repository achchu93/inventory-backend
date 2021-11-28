from rest_framework import viewsets

from InventoryApp.models import InventoryReport
from InventoryApp.serializers import InventoryReportSerializer

class InventoryReportViewSet(viewsets.ModelViewSet):
	queryset = InventoryReport.objects.all()
	serializer_class = InventoryReportSerializer
