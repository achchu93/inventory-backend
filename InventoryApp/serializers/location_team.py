from rest_framework import serializers

from InventoryApp.models import User, LocationTeam

class LocationTeamSeralizer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=False, required=True, queryset=User.objects.all())

	class Meta:
		model = LocationTeam
		fields = ['user', 'is_manager']
