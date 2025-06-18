from rest_framework.routers import DefaultRouter
from django.urls import path
from .import views

router = DefaultRouter()
router.register(r'medicinecategory',views.MedicineCategoryViewSet)
router.register(r'medicine',views.MedicineViewSet)
router.register(r'medicineprescription',views.MedicinePrescriptionViewSet)

urlpatterns = router.urls