from django.shortcuts import render
from .serializers import (
    MedicineCategorySerializer,
    MedicineSerializer,
    MedicineStockSerializer,
)
from .models import MedicineCategory, Medicine, MedicinePrescription, MedicineStock
from .serializers import AppointmentSerializer,PatientSerializers
from .models import Doctor,Appointment,Patient
from rest_framework import viewsets, permissions, filters
from .models import Role,Staff,Specialization
from .serializers import RoleSerializer,StaffSerializer,SpecializationSerializer,DoctorSerializer
from .models import Consultation,LabTest,LabTestCategory,LabTestPrescription
from .serializers import ConsultaionSerializer,LabTestSerializer,LabTestCategorySerializer,LabTestPrescriptionSerializer
from .serializers import MedicinePrescriptionSerializer
from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

# Create your views here.
class MedicineCategoryViewSet(viewsets.ModelViewSet):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineStockViewSet(viewsets.ModelViewSet):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer

class MedicinePrescriptionViewSet(viewsets.ModelViewSet):   
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer           

class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializers
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
    
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
