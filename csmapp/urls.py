from rest_framework.routers import DefaultRouter
from django.urls import path
from .import views

router = DefaultRouter()
router.register(r'medicinecategory',views.MedicineCategoryViewSet)
router.register(r'medicinestock',views.MedicineStockViewSet)
router.register(r'medicine',views.MedicineViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'appoinment', views.AppointmentViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'specialization', views.SpecializationViewSet)
router.register(r'doctor', views.DoctorViewSet)
router.register(r'consultation', views.ConsultationViewSet)
router.register(r'labtest', views.LabTestViewSet)
router.register(r'labtestcategory', views.LabTestCategory)
router.register(r'medicineprescriptions',views.MedicinePrescriptionViewSet)
router.register(r'labtestprescriptions',views.LabTestPrescriptionViewSet)
urlpatterns = router.urls
