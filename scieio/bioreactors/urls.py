from django.urls import path, include
from rest_framework import routers
from scieio.bioreactors import views

router = routers.DefaultRouter()
router.register('list', views.BioReactorViewSet)

app_name = "bioreactors"
urlpatterns = [
    path('', include(router.urls)),
]
