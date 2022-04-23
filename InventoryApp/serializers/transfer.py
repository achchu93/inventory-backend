from rest_framework import serializers

from InventoryApp.models import Transfer, TransferItem, Location, User
from .transfer_item import TransferItemSerializer
from InventoryApp.serializers import LocationSerializer, UserSerializer

class TransferSerializer(serializers.ModelSerializer):
	items = TransferItemSerializer(many=True, source='transferitem_set')

	class Meta:
		model = Transfer
		fields = ['id','requested_by', 'to_location', 'from_location', 'date_time', 'status', 'note', 'items']
		extra_kwargs = {
			'date_time': {'required': True},
			'requested_by': {'required': True, 'read_only': False},
			'to_location': {'required': True, 'read_only': False},
			'from_location': {'required': True, 'read_only': False},
			'items': {'required': True, 'read_only': False, 'many': True, 'queryset': TransferItem.objects.all()}
		}

	def create(self, validated_data):
		items = []
		if 'transferitem_set' in validated_data:
			items = validated_data.pop('transferitem_set')
		transfer = Transfer.objects.create(**validated_data)
		for item_data in items:
			TransferItem.objects.create(transfer=transfer, item=item_data['item'], requested_quantity=item_data['requested_quantity'])
		return transfer

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			if(key == 'transferitem_set'):
				instance.items.clear()
				items = list({object_['item']: object_ for object_ in validated_data.get('transferitem_set', [])}.values()) # get unique items by id
				for item_data in items:
					TransferItem.objects.create(transfer=instance, item=item_data['item'], requested_quantity=item_data['requested_quantity'])
			else:
				setattr(instance, key, value)

		instance.save()
		return instance


	def validate_items(self, value):
		if len(value) < 1:
			raise serializers.ValidationError("Transfer should have at least 1 item")
		return value

	def to_internal_value(self, data):
		if 'items' in data:
			if not isinstance(data.get('items', []), list):
				raise serializers.ValidationError({
					'items': ['Expected a list of items but got type {input_type}'.format(input_type=type(data.get('items')).__name__)]
				})
		return super().to_internal_value(data)

	def to_representation(self, instance):
		data = super().to_representation(instance)

		if data.get('to_location'):
			data['to_location'] = LocationSerializer(Location.objects.get(id=data.get('to_location'))).data

		if data.get('requested_by'):
			data['requested_by'] = UserSerializer(User.objects.get(id=data.get('requested_by'))).data

		return data
