from django.db import models

from InventoryApp.models import Transfer, Item

class TransferItem(models.Model):
	transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	requested_quantity = models.IntegerField()

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'transfer_item'
		unique_together = [['transfer', 'item']]
