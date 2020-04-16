from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.ChromaCategoryViewSet)
router.register('gas-chromatography', views.GCChromaViewSet)
router.register('liquid-chromatography', views.LCChromaViewSet)
router.register('gc-systems', views.GCSystemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
