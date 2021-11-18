from django.db import models
from .item_category import ItemCategory

class Item(models.Model):
	STATUSES = [
		(1, 'Active'),
		(0, 'Inactive')
	]
	DEFAULT_STATUS = 1

	name = models.CharField(max_length=255)
	quantity = models.IntegerField(null=True)
	last_bought_price = models.FloatField(null=True)
	order_by = models.DateTimeField(null=True)
	file_name = models.CharField(max_length=255, null=True)
	status = models.CharField(max_length=2, choices=STATUSES)
	category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'item'
