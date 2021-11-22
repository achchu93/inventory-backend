from django.db import models

from InventoryApp.models import Order, Item

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	price = models.FloatField()

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'order_item'
		unique_together = [['order', 'item']]
