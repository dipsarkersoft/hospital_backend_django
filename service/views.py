from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSer


class ServiceViewset(viewsets.ModelViewSet):
    queryset=Service.objects.all()
    serializer_class=ServiceSer
    
