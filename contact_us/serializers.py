from rest_framework import serializers
from .models import ContactUs

class Contact_UsSerializar(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields='__all__'