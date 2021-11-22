from rest_framework import serializers

from InventoryApp.models import Order, OrderItem
from .order_item import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
	items = OrderItemSerializer(many=True, source='orderitem_set')

	class Meta:
		model = Order
		fields = ['id','number', 'total', 'credits_issued', 'paid', 'expected_delivery', 'payment_type', 'date', 'status', 'note', 'ordered_by', 'location', 'vendor', 'items']
		extra_kwargs = {
			'ordered_by': {'required': True, 'read_only': False},
			'location': {'required': True, 'read_only': False},
			'vendor': {'required': True, 'read_only': False},
			'items': {'required': True, 'read_only': False, 'many': True, 'queryset': OrderItem.objects.all()}
		}

	def create(self, validated_data):
		print(validated_data)
		items = []
		if 'orderitem_set' in validated_data:
			items = validated_data.pop('orderitem_set')
		order = Order.objects.create(**validated_data)
		for item_data in items:
			OrderItem.objects.create(order=order, item=item_data['item'], quantity=item_data['quantity'], price=item_data['price'])
		return order


	def validate_items(self, value):
		if len(value) < 1:
			raise serializers.ValidationError("Order should have at least 1 item")
		return value

	def to_internal_value(self, data):
		if 'items' in data:
			if not isinstance(data.get('items', []), list):
				raise serializers.ValidationError({
					'items': ['Expected a list of items but got type {input_type}'.format(input_type=type(data.get('items')).__name__)]
				})
		return super().to_internal_value(data)
