from django.urls import path, include
from rest_framework import routers
from scieio.analytical_instruments import views

router = routers.DefaultRouter()
router.register('categories', views.InstrumentationViewSet)

app_name = "analytical_instruments"
urlpatterns = [
    path('', include(router.urls)),
]
