from django_filters import rest_framework as filters
from InventoryApp.models import Transfer

class TransferFilter(filters.FilterSet):
	class Meta:
		model = Transfer
		fields = {
			'requested_by': ['exact', 'in'],
			'status': ['exact', 'in'],
			'date_time': ['exact', 'gt', 'lt' ]
		}
