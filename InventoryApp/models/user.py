from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	username = None
	email = models.EmailField(max_length=100, unique=True)
	password = models.CharField(max_length=255)
	address = models.CharField(max_length=500, default='')
	phone = models.CharField(max_length=15, default='')
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = None
	date_joined = None
	is_superuser = None
	groups = None
	user_permissions = None

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['password']

	class Meta:
		app_label = 'InventoryApp'
		db_table = 'user'
