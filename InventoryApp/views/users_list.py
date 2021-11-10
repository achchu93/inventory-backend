from django.db.models.query import QuerySet
from rest_framework.serializers import Serializer
from InventoryApp.models import User
from InventoryApp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
