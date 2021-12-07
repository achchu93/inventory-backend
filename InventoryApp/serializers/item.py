from rest_framework import serializers

from InventoryApp.models import Item
from .item_category import ItemCategorySerializer

class ItemSerializer(serializers.ModelSerializer):
	category = ItemCategorySerializer()
	class Meta:
		model = Item
		fields = ['id', 'name', 'quantity', 'last_bought_price', 'order_by', 'file_name', 'status', 'category']
		extra_kwargs = {
			'category': { 'required': True, 'read_only': False }
		}
