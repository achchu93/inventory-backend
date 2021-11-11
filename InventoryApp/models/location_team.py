from django.db import models

from InventoryApp.models import Location, User

class LocationTeam(models.Model):
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_manager = models.BooleanField(default=False)

	class Meta:
		app_label = 'InventoryApp'
		unique_together = [['location', 'user']]
		db_table = 'location_team'
