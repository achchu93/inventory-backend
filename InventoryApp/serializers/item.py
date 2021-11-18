from rest_framework import serializers

from InventoryApp.models import Item

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['id', 'name', 'quantity', 'last_bought_price', 'order_by', 'file_name', 'status', 'category']
		extra_kwargs = {
			'category': { 'required': True, 'read_only': False }
		}
