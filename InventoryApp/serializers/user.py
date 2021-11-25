from rest_framework import serializers

from InventoryApp.models import User

class UserSerializer(serializers.ModelSerializer):
	locations = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
	class Meta:
		model = User
		fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone', 'is_active', 'is_admin', 'address', 'locations']
		extra_kwargs = {
			'password': {'write_only': True, 'required': False},
			'first_name': {'required': True},
			'last_name': {'required': True}
		}

	def create(self, validated_data):
		if( 'password' in validated_data ):
			validated_data.pop('password') # pop out the password field to generate internally

		password = User.objects.make_random_password(length=12)

		user = User(**validated_data)
		user.set_password(password)
		user.save()
		user.email_user( 'Welcome to the Inventory APP.', 'Your password is %s' % password )
		return user

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			if(key == 'password'):
				instance.set_password(value)
			else:
				setattr(instance, key, value)
		instance.save()
		return instance

	def validate_password(self, value):
		method = self.context['request'].method;
		if method in ['PUT', 'PATCH'] and len(value) < 8:
			raise serializers.ValidationError('Must be 8-12 length')
		return value
