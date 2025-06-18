

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Consultation,LabTest,LabTestCategory,LabTestPrescription
from .serializers import ConsultaionSerializer,LabTestSerializer,LabTestCategorySerializer,LabTestPrescriptionSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset=Consultation.objects.all()
    serializer_class=ConsultaionSerializer

class LabTestViewSet(viewsets.ModelViewSet):
    queryset=LabTest.objects.all()
    serializer_class=LabTestSerializer

class LabTestCategory(viewsets.ModelViewSet):
    queryset=LabTestCategory.objects.all()
    serializer_class=LabTestCategorySerializer

class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    queryset=LabTestPrescription.objects.all()
    serializer_class=LabTestPrescriptionSerializer    