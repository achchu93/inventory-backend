from rest_framework import serializers

from InventoryApp.models import InventoryReportItem,Item, Location
from .item import ItemSerializer
from .location import LocationSerializer

class InventoryReportItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Item.objects.all())
	location = serializers.PrimaryKeyRelatedField(read_only=True, required=False, source='inventory_report.location')

	class Meta:
		model = InventoryReportItem
		fields = ['item', 'quantity', 'location']

	def to_representation(self, instance):
		original_data = super().to_representation(instance)
		print(repr(original_data))
		item = Item.objects.get(id=original_data.get('item'))

		data = ItemSerializer(item).data
		data['quantity'] = original_data.get('quantity')
		data['location'] = original_data.get('location');

		return data

