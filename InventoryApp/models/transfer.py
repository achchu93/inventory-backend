from django.db import models
from django.utils.timezone import now

from InventoryApp.models import Location, User, Item

class Transfer(models.Model):
	STATUSES = [
		(1, 'Process'),
		(2, 'Completed'),
		(3, 'Hold')
	]

	date_time = models.DateTimeField(default=now)
	status = models.CharField(max_length=2, choices=STATUSES, null=True)
	note = models.CharField(max_length=255, null=True)
	requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
	from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='from_location')
	to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='to_location', null=True)
	items = models.ManyToManyField(Item, through='TransferItem', related_name='transfers')

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'transfer'
