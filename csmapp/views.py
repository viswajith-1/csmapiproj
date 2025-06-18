

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Consultation,LabTest,LabTestCategory,LabTestPrescription
from .serializers import ConsultaionSerializer,LabTestSerializer,LabTestCategorySerializer,LabTestPrescriptionSerializer
from .serializers import MedicinePrescriptionSerializer,LabTestPrescriptionSerializer
from .models import MedicinePrescription,LabTestPrescription

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset=Consultation.objects.all()
    serializer_class=ConsultaionSerializer

class LabTestViewSet(viewsets.ModelViewSet):
    queryset=LabTest.objects.all()
    serializer_class=LabTestSerializer

class LabTestCategory(viewsets.ModelViewSet):
    queryset=LabTestCategory.objects.all()
    serializer_class=LabTestCategorySerializer  

# Create your views here.

class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    queryset=MedicinePrescription.objects.all()
    serializer_class=MedicinePrescriptionSerializer

class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    queryset=LabTestPrescription.objects.all()
    serializer_class=LabTestPrescriptionSerializer
