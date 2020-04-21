from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('list', views.ImmunoAssayViewSet)

app_name = "immunoassay"
urlpatterns = [
    path('', include(router.urls)),
]
