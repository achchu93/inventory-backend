from django.db.models import fields
from rest_framework import serializers
from InventoryApp.models import Location

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = '__all__'
