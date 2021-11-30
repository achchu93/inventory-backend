from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now

from InventoryApp.models import Order

class Receipt(models.Model):
	number = models.CharField(max_length=255)
	date_time = models.DateTimeField(default=now, null=True)
	amount = models.FloatField(null=True)
	order = models.ForeignKey(Order, on_delete=CASCADE)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'receipt'
