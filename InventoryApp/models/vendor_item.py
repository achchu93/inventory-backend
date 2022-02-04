from django.db import models

from InventoryApp.models import Vendor, Item

class VendorItem(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'vendor_item'
		unique_together = [['vendor', 'item']]
