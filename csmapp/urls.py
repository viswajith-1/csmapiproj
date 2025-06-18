from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path


router = DefaultRouter()
router.register(r'consultation', views.ConsultationViewSet)
router.register(r'labtest', views.LabTestViewSet)
router.register(r'labtestcategory', views.LabTestCategory)
router.register(r'labtestprescription', views.LabTestPrescriptionViewSet)
urlpatterns = router.urls