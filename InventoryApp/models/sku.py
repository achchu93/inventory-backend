from django.db import models
from .item import Item

class Sku(models.Model):
	sku = models.CharField(max_length=255)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'sku'
