from rest_framework import serializers

from InventoryApp.models import InventoryReportItem,Item
from InventoryApp.serializers import ItemSerializer

class InventoryReportItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Item.objects.all())

	class Meta:
		model = InventoryReportItem
		fields = ['item', 'quantity']

	def to_representation(self, instance):
		data = super().to_representation(instance)
		item = Item(id=data['item'])
		data['item'] = ItemSerializer(item).data

		return data
