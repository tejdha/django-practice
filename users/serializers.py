from rest_framework import serializers
# from .models import user
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','password','confirm_password']

    
    def validate(self, data):

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                "Invalid, password does not matched"
            )
        return data
    
    def create(self, validate_data ):
        validate_data.pop('confirm_password')
        return User.objects.create(username=validate_data['username'],password=validate_data['password'])