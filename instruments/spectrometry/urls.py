from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.SpectrometryViewSet)
router.register('gas-MS', views.GasMSViewSet)
router.register('liquid-MS', views.LiquidMSViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
