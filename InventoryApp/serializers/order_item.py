from rest_framework import serializers

from InventoryApp.models import OrderItem,Item
from InventoryApp.serializers import ItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Item.objects.all())

	class Meta:
		model = OrderItem
		fields = ['item', 'quantity', 'price']
		extra_kwargs = {
		}

	def to_representation(self, instance):
		data = super().to_representation(instance)
		item = Item.objects.get(pk=data['item'])
		data['item'] = ItemSerializer(item).data

		return data

