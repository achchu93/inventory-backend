from rest_framework import serializers

from InventoryApp.models import InventoryReport, InventoryReportItem
from .inventory_report_item import InventoryReportItemSerializer

class InventoryReportSerializer(serializers.ModelSerializer):
	items = InventoryReportItemSerializer(many=True, source='inventoryreportitem_set')

	class Meta:
		model = InventoryReport
		fields = ['id','started_at', 'started_by', 'closed_at', 'closed_by', 'location', 'items']
		extra_kwargs = {
			'started_by': {'required': True, 'read_only': False},
			'closed_by': {'required': True, 'read_only': False},
			'closed_at': {'required': False},
			'items': {'required': True, 'read_only': False, 'many': True, 'queryset': InventoryReportItem.objects.all()}
		}

	def create(self, validated_data):
		items = []
		if 'inventoryreportitem_set' in validated_data:
			items = validated_data.pop('inventoryreportitem_set')
		inventory_report = InventoryReport.objects.create(**validated_data)
		for item_data in items:
			InventoryReportItem.objects.create(inventory_report=inventory_report, item=item_data['item'], quantity=item_data['quantity'])
		return inventory_report

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			if(key == 'inventoryreportitem_set'):
				instance.items.clear()
				items = list({object_['item']: object_ for object_ in validated_data.get('inventoryreportitem_set', [])}.values()) # get unique items by id
				for item_data in items:
					InventoryReportItem.objects.create(inventory_report=instance, item=item_data['item'], quantity=item_data['quantity'])
			else:
				setattr(instance, key, value)

		instance.save()
		return instance


	def validate_items(self, value):
		if len(value) < 1:
			raise serializers.ValidationError("Inventory Report should have at least 1 item")
		return value

	def to_internal_value(self, data):
		if 'items' in data:
			if not isinstance(data.get('items', []), list):
				raise serializers.ValidationError({
					'items': ['Expected a list of items but got type {input_type}'.format(input_type=type(data.get('items')).__name__)]
				})
		return super().to_internal_value(data)
