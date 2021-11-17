from django.db import models

from .vendor_category import VendorCategory

class Vendor(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(null=True, blank=True)
	address = models.CharField(max_length=255, null=True)
	phone = models.CharField(max_length=255, null=True)
	is_active = models.BooleanField(default=True)
	category = models.ForeignKey(VendorCategory, on_delete=models.CASCADE, null=True)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'vendor'
