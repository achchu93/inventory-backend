from django.db import models
from django.utils.timezone import now

from InventoryApp.models import Location, User, Vendor, Item

class Order(models.Model):
	PAYMENT_TYPES = [
		('COD', 'Cash On Delivery'),
		('STRIPE', 'Stripe Credit/Debit'),
		('PAYPAL', 'Paypal')
	]

	STATUSES = [
		(1, 'Process'),
		(2, 'Completed'),
		(3, 'Hold')
	]

	number = models.CharField(max_length=255)
	total = models.FloatField(null=True)
	credits_issued = models.FloatField(null=True)
	paid = models.FloatField(null=True)
	expected_delivery = models.DateTimeField(null=True)
	payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPES, null=True)
	date = models.DateTimeField(default=now)
	status = models.CharField(max_length=2, choices=STATUSES)
	note = models.CharField(max_length=255, null=True)
	ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	items = models.ManyToManyField(Item, through='OrderItem', related_name='orders')

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'order'
