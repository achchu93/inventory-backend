from rest_framework import serializers

from InventoryApp.models import TransferItem,Item
from InventoryApp.serializers import ItemSerializer

class TransferItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Item.objects.all())

	class Meta:
		model = TransferItem
		fields = ['item', 'requested_quantity']

	def to_representation(self, instance):
		data = super().to_representation(instance)
		item = Item.objects.get(id=data['item'])
		data['item'] = ItemSerializer(item).data

		return data

