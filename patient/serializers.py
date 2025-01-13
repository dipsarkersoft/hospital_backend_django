from rest_framework import serializers

from .models import Patient
from django.contrib.auth.models import User

class PatientSer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=Patient
        fields='__all__'
        


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','confirm_password']


    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        if password !=confirm_password:
            raise serializers.ValidationError({'error':'Password and Confirm Pass doesnt Match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'Email Alear Exists'})
        
        account=User(username=username,email=email,first_name=first_name,last_name=last_name)
        print(account)
        account.set_password(password)
        account.is_active=False
        account.save()
        return account



                       

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)