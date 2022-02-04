from rest_framework import serializers

from InventoryApp.models import VendorItem,Item, Vendor
from InventoryApp.serializers import ItemSerializer

class VendorItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, many=False, queryset=Item.objects.all())

	class Meta:
		model = VendorItem
		fields = ['vendor', 'item',]
		extra_kwargs = {
		}

	def to_representation(self, instance):
		data = super().to_representation(instance)
		item = Item.objects.get(id=data['item'])
		data = ItemSerializer(item).data

		return data

