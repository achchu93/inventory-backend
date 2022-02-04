from rest_framework import serializers

from InventoryApp.models import VendorItem,Item, Vendor
from InventoryApp.serializers import VendorSerializer

class ItemVendorsSerializer(serializers.ModelSerializer):
	vendor = serializers.PrimaryKeyRelatedField(read_only=False, required=True, many=False, queryset=Item.objects.all())

	class Meta:
		model = VendorItem
		fields = ['vendor', 'item',]
		extra_kwargs = {
		}

	def to_representation(self, instance):
		data = super().to_representation(instance)
		vendor = Vendor.objects.get(id=data['vendor'])
		data = VendorSerializer(vendor).data

		return data

