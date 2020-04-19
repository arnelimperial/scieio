from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.ElectrophorosisCategoryViewSet)
# router.register('gc', views.GCChromaViewSet)
# router.register('lc', views.LCChromaViewSet)
# router.register('gas-chromatography', views.GCSystemViewSet)
# router.register('liquid-chromatography', views.LCViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
