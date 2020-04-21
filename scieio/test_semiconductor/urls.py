from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.TestSemiconductorViewSet)


app_name ="test_semiconductor"
urlpatterns = [
    path('', include(router.urls)),
]
