from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .models import Appoinment
from .serializers import AppoinmentSer

class AppoinmentViewset(viewsets.ModelViewSet):

    queryset= Appoinment.objects.all()
    serializer_class=AppoinmentSer

    def get_queryset(self):
        queryset=super().get_queryset()
        patient_id=self.request.query_params.get('patient_id')
        if patient_id:
          queryset=queryset.filter(patient_id=patient_id)
        return queryset
    
    def get_queryset(self):
        queryset=super().get_queryset()
        doctor_id=self.request.query_params.get('doctor_id')
        if doctor_id :
            queryset=queryset.filter(doctor_id=doctor_id)
        return queryset    
    
    