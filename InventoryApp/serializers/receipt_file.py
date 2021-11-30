from django.db.models import fields
from rest_framework import serializers

from InventoryApp.models import ReceiptFile, Receipt, User

class ReceiptFileSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReceiptFile
		fields = '__all__'
		extra_kwargs = {
			'receipt': {
				'required': True, 'read_only': False, 'many': False, 'queryset': Receipt.objects.all()
			},
			'uploaded_by': {
				'required': True, 'read_only': False, 'many': False, 'queryset': User.objects.all()
			}
		}
