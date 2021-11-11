from rest_framework import serializers

from InventoryApp.models import User
from .location import LocationSerializer

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
		extra_kwargs = {
			'password': {'write_only': True},
			'is_admin': {'read_only': True},
			'is_active': {'read_only': True},
		}

	def create(self, validated_data):
		user = User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		instance.set_password(validated_data['password'])
		instance.save()
		return instance
