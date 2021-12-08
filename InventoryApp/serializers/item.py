from rest_framework import serializers

from InventoryApp.models import Item, ItemCategory
from .item_category import ItemCategorySerializer

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['id', 'name', 'quantity', 'last_bought_price', 'order_by', 'file_name', 'status', 'category']
		extra_kwargs = {
			'category': { 'required': True, 'read_only': False }
		}

	def to_representation(self, instance):
		data = super().to_representation(instance)

		if data.get('category'):
			data['category'] = ItemCategorySerializer(ItemCategory.objects.get(id=data.get('category'))).data

		return data
