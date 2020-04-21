from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('list', views.VRViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
