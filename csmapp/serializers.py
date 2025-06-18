from rest_framework import serializers
from .models import MedicinePrescription,LabTestPrescription

class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicinePrescription
        fields='__all__'

class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTestPrescription
        fields='__all__'