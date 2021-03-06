from django.urls import path, include
from rest_framework import routers
from scieio.biotechnology import views

router = routers.DefaultRouter()
router.register('list', views.BioTechViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
