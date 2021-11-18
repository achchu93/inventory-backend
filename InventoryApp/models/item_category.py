from django.db import models

class ItemCategory(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'item_category'
