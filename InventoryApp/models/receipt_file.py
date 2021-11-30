from django.db import models
from django.utils.timezone import now

from InventoryApp.models import User, Receipt

class ReceiptFile(models.Model):
	file_name = models.CharField(max_length=255)
	file_name_on_server = models.CharField(max_length=255)
	uploaded_at = models.DateTimeField(default=now)
	uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
	receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'receipt_file'
