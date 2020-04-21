from django.urls import path, include
from rest_framework import routers
from scieio.chromatography import views

router = routers.DefaultRouter()
router.register('categories', views.ChromaCategoryViewSet)
router.register('gc', views.GCChromaViewSet)
router.register('lc', views.LCChromaViewSet)
router.register('gas-chromatography', views.GCSystemViewSet)
router.register('liquid-chromatography', views.LCViewSet)

app_name = "chromatography"
urlpatterns = [
    path('', include(router.urls)),
]
