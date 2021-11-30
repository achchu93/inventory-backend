from rest_framework import serializers

from InventoryApp.models import Receipt, Order

class ReceiptSerializer(serializers.ModelSerializer):

	class Meta:
		model = Receipt
		fields = '__all__'
		extra_kwargs = {
			'order': {
				'required': True, 'read_only': False, 'many': False, 'queryset': Order.objects.all()
			}
		}
