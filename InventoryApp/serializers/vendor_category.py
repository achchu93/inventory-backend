from rest_framework import serializers

from InventoryApp.models import VendorCategory

class VendorCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = VendorCategory
		fields = [ 'id', 'name' ]
