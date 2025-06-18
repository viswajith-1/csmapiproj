from django.shortcuts import render
from .serializers import MedicinePrescriptionSerializer,LabTestPrescriptionSerializer
from rest_framework import viewsets
from .models import MedicinePrescription,LabTestPrescription
# Create your views here.

class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    queryset=MedicinePrescription.objects.all()
    serializer_class=MedicinePrescriptionSerializer

class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    queryset=LabTestPrescription.objects.all()
    serializer_class=LabTestPrescriptionSerializer