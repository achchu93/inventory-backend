from django.db import models

from InventoryApp.models import InventoryReport, Item

class InventoryReportItem(models.Model):
	inventory_report = models.ForeignKey(InventoryReport, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'inventory_report_item'
		unique_together = [['inventory_report', 'item']]
