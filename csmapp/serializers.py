from rest_framework import serializers
from .models import Consultation,LabTest,LabTestCategory,LabTestPrescription
from .models import MedicinePrescription,LabTestPrescription
class ConsultaionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultation
        fields='__all__'
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTest
        fields='__all__'
class LabTestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTestCategory
        fields='__all__'


class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicinePrescription
        fields='__all__'

class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTestPrescription
        fields='__all__'