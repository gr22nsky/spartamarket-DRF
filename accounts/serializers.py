from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'last_name', 'first_name', 'nickname', 'birth', 'gender', 'introduction')
