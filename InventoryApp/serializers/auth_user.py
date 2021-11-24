from rest_framework import serializers

from InventoryApp.models import User
from InventoryApp.serializers import UserSerializer

class AuthUserSerializer(serializers.Serializer):
	class Meta:
		model = User
		fields = ['id', 'name', 'quantity', 'last_bought_price', 'order_by', 'file_name', 'status', 'category']
		extra_kwargs = {
			'category': { 'required': True, 'read_only': False }
		}

	def validate(self, attrs):
		return super().validate(attrs)
