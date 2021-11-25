from rest_framework import serializers
from InventoryApp.models import Location, LocationTeam, location
from .location_team import LocationTeamSeralizer

class LocationSerializer(serializers.ModelSerializer):
	users = LocationTeamSeralizer(source='locationteam_set', required=False, many=True, read_only=False)
	class Meta:
		model = Location
		fields = ['id', 'name', 'email', 'address', 'phone', 'is_active', 'users', 'hours']
		extra_kwargs = {
			'address': { 'required': True },
			'users': { 'queryset': LocationTeam.objects.all() }

		}

	def create(self, validated_data):
		users = []
		if 'locationteam_set' in validated_data:
			users = validated_data.pop('locationteam_set')
		location = Location.objects.create(**validated_data)
		for user_data in users:
			LocationTeam.objects.create(location=location, user=user_data['user'], is_manager=user_data.get('is_manager', False))
		return location

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			if(key == 'locationteam_set'):
				instance.users.clear()
				users = list({object_['user']: object_ for object_ in validated_data.get('locationteam_set', [])}.values()) # get unique items by id
				for user_data in users:
					LocationTeam.objects.create(location=instance, user=user_data['user'], is_manager=user_data.get('is_manager', False))
			else:
				setattr(instance, key, value)

		instance.save()
		return instance
