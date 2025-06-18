from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Role,Staff,Specialization,Doctor
from .serializers import RoleSerializer,StaffSerializer,SpecializationSerializer,DoctorSerializer
from .models import Consultation,LabTest,LabTestCategory,LabTestPrescription
from .serializers import ConsultaionSerializer,LabTestSerializer,LabTestCategorySerializer,LabTestPrescriptionSerializer
from .serializers import MedicinePrescriptionSerializer,LabTestPrescriptionSerializer
from .models import MedicinePrescription,LabTestPrescription
from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=SpecializationSerializer
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset=Consultation.objects.all()
    serializer_class=ConsultaionSerializer

class LabTestViewSet(viewsets.ModelViewSet):
    queryset=LabTest.objects.all()
    serializer_class=LabTestSerializer

class LabTestCategory(viewsets.ModelViewSet):
    queryset=LabTestCategory.objects.all()
    serializer_class=LabTestCategorySerializer  

class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    queryset=MedicinePrescription.objects.all()
    serializer_class=MedicinePrescriptionSerializer

class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    queryset=LabTestPrescription.objects.all()
    serializer_class=LabTestPrescriptionSerializer
