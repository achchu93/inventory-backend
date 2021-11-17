from django.db import models

from InventoryApp.models import User

class Location(models.Model):
	name = models.CharField(max_length=255)
	hours = models.CharField(max_length=255, null=True, blank=True)
	email = models.EmailField(unique=True)
	address = models.CharField(max_length=255, default='')
	phone = models.CharField(max_length=255, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	users = models.ManyToManyField(User, through='LocationTeam', related_name='locations')

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'location'
