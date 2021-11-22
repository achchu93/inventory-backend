from rest_framework import serializers

from InventoryApp.models import OrderItem,Item

class OrderItemSerializer(serializers.ModelSerializer):
	item = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=Item.objects.all())

	class Meta:
		model = OrderItem
		fields = ['item', 'quantity', 'price']
		extra_kwargs = {
		}
