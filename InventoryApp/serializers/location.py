from rest_framework import serializers
from InventoryApp.models import Location
from InventoryApp.models.user import User

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ['id', 'name', 'email', 'address', 'phone', 'is_active', 'users', 'hours']
		extra_kwargs = {
			'address': { 'required': True },
			'users': { 'required': False, 'read_only': False, 'many': True, 'queryset': User.objects.all() }
		}

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			if(key == 'users'):
				instance.users.clear()
				users = validated_data.get('users', [])
				for user in users:
					instance.users.add(user)
			else:
				setattr(instance, key, value)

		instance.save()
		return instance
