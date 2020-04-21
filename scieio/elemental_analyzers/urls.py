from django.urls import path, include
from rest_framework import routers
from scieio.elemental_analyzers import views

router = routers.DefaultRouter()
router.register('list', views.ElementalAnalyzerViewSet)

app_name = "elemental_analyzers"
urlpatterns = [
    path('', include(router.urls)),
]

