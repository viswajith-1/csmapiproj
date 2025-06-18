from django.shortcuts import render
from .serializers import (
    MedicineCategorySerializer,
    MedicineSerializer,
    MedicinePrescriptionSerializer,
    MedicineStockSerializer,
)
from rest_framework import viewsets
from .models import MedicineCategory, Medicine, MedicinePrescription, MedicineStock

# Create your views here.
class MedicineCategoryViewSet(viewsets.ModelViewSet):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicinePrescriptionViewSet(viewsets.ModelViewSet):   
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer           