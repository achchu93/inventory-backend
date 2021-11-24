from rest_framework import generics
from rest_framework.response import Response

from InventoryApp.models import User
from InventoryApp.serializers import UserSerializer

class AuthUserView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		user = UserSerializer(request.user);
		return Response(user.data)


