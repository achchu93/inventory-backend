from rest_framework import serializers

from InventoryApp.models import Sku

class SkuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sku
		fields = ['id', 'sku', 'item']
		extra_kwargs = {
			'item': { 'required': True, 'read_only': False }
		}
