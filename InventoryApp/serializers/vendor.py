from rest_framework import serializers

from InventoryApp.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vendor
		fields = [ 'id', 'name', 'email', 'address', 'phone', 'is_active', 'category' ]
		extra_kwargs = {
			'is_active': {'required': True},
			'category_id': {'required': False}
		}
