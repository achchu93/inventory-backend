from rest_framework import serializers

from InventoryApp.models import InventoryReportItem,Item
from InventoryApp.serializers import ItemSerializer

class InventoryReportItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Item.objects.all())

	class Meta:
		model = InventoryReportItem
		fields = ['item', 'quantity']

	def to_representation(self, instance):
		original_data = super().to_representation(instance)
		item = Item.objects.get(id=original_data.get('item'))

		data = ItemSerializer(item).data
		data['quantity'] = original_data.get('quantity')

		return data

