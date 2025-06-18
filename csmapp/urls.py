from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path

router=DefaultRouter()
router.register(r'medicineprescriptions',views.MedicinePrescriptionViewSet)
router.register(r'labtestprescriptions',views.LabTestPrescriptionViewSet)
urlpatterns = router.urls
