from rest_framework import serializers
from .models import Appointment,Patient
from .models import Role,Staff,Specialization,Doctor
from .models import Consultation,LabTest,LabTestCategory,LabTestPrescription
from .models import MedicinePrescription,LabTestPrescription



#sonu
class PatientSerializers(serializers.ModelSerializer):
   class Meta:
       model= Patient
       fields = '__all__'
       
class AppointmentSerializer(serializers.ModelSerializer):
   class Meta:
       model= Appointment
       fields = '__all__'
       

    
#sangeeth
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specialization
        fields='__all__'
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

#shambu
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
        
#viswajith
class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicinePrescription
        fields='__all__'

class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabTestPrescription
        fields='__all__'
