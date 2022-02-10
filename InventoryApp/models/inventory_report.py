from django.db import models

from InventoryApp.models import Location, User, Item

class InventoryReport(models.Model):
	STATUSES = [
		(1, 'Process'),
		(2, 'Completed'),
		(3, 'Hold')
	]

	started_at = models.DateTimeField()
	closed_at = models.DateTimeField(null=True)
	status = models.CharField(max_length=2, choices=STATUSES)
	started_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='started_by')
	closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='closed_by', null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	items = models.ManyToManyField(Item, through='InventoryReportItem', related_name='inventory_reports')

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'inventory_report'
