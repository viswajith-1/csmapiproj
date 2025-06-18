from rest_framework import serializers  
from .models import Medicine, MedicineCategory, MedicinePrescription, MedicineStock
class MedicineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineCategory
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    MedicineCategoryId = MedicineCategorySerializer(read_only=True)

    class Meta:
        model = Medicine
        fields = '__all__'

class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    MedicineId = MedicineSerializer(read_only=True)

    class Meta:
        model = MedicinePrescription
        fields = '__all__'

class MedicineStockSerializer(serializers.ModelSerializer):
    MedicineId = MedicineSerializer(read_only=True)

    class Meta:
        model = MedicineStock
        fields = '__all__'  