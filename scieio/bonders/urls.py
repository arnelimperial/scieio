from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('list', views.BonderViewSet)

app_name = "bonders"
urlpatterns = [
    path('', include(router.urls)),
]
