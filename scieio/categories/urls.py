from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('list', views.CategoryViewSet)

app_name = "categories"
urlpatterns = [
    path('', include(router.urls)),
]
