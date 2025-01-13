from django.shortcuts import render
from rest_framework import viewsets
from .models import Speacialization,Review,AvailableTime,Desigation,Doctor
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters,pagination



class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100


class DoctorViewset(viewsets.ModelViewSet):
     
    queryset=Doctor.objects.all()
    pagination_class=DoctorPagination
    serializer_class=serializers.DoctorSer


class SpeacializationViewset(viewsets.ModelViewSet):
    queryset=Speacialization.objects.all()
    serializer_class=serializers.SpeacializationSer

class DesigationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]                                
    queryset=Desigation.objects.all()
    serializer_class=serializers.DesigationSer

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSer

class ReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=serializers.ReviewSer
    
