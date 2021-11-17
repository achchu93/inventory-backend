from rest_framework import serializers
from InventoryApp.models import Location
from InventoryApp.models.user import User

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ['id', 'name', 'email', 'address', 'phone', 'is_active', 'users']
		extra_kwargs = {
			'address': { 'required': True },
			'users': { 'required': False, 'read_only': False, 'many': True, 'queryset': User.objects.all() }
		}

	def update(self, instance, validated_data):
		if 'users' in validated_data:
			instance.users.clear()
			users = validated_data.get('users', [])
			for user in users:
				instance.users.add(user)
			instance.save()
		return instance
