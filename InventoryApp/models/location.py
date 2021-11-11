from django.db import models

from InventoryApp.models import User

class Location(models.Model):
	name = models.CharField(max_length=255, default='')
	hours = models.CharField(max_length=255, default='')
	email = models.EmailField(unique=True)
	address = models.CharField(max_length=255, default='')
	phone = models.CharField(max_length=255, default='')
	is_active = models.BooleanField(default=True)
	users = models.ManyToManyField(User, through='LocationTeam')

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'location'
