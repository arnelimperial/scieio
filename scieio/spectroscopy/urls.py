from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.SpectroscopyViewSet)
router.register('atomic-absorption', views.AtomicAbsorptionViewSet)
router.register('spectrophotometer', views.SpectrophotometerViewSet)
router.register('icp', views.ICPViewSet)
router.register('ftir', views.FTIRViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
