from .models import CustomUser, Home, Role
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # Serializer for User model
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'surname', 'password', 'document', 'date_of_birth', 'home', 'roles', 'status', 'created_at',)
        extra_kwargs = {'password': {'write_only': True}, 'created_at': {'read_only': True}}

    def create(self, validated_data):
        required_fields = ['email', 'name', 'surname', 'document', 'date_of_birth', 'home', 'roles']
        errors = {}

        for field in required_fields:
            if not validated_data.get(field):
                errors[field] = 'This field is required'
        if errors:
            raise serializers.ValidationError(errors)

        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            document=validated_data['document'],
            date_of_birth=validated_data['date_of_birth'],
            home=validated_data['home'],
        )
        user.set_password(validated_data['password'])
        user.save()
        user.roles.set(validated_data['roles'])
        user.save()
        return user


class HomeSerializer(serializers.ModelSerializer):
    # Serializer for Location model
    class Meta:
        model = Home
        fields = ('id', 'name', 'address')


class RoleSerializer(serializers.ModelSerializer):
    # Serializer for Role model
    class Meta:
        model = Role
        fields = ('id', 'name')
