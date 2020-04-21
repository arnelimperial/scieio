from django.urls import path, include
from rest_framework import routers
from scieio.sellers import views

router = routers.DefaultRouter()
router.register('list', views.SellerViewSet)

app_name = "sellers"
urlpatterns = [
    path('', include(router.urls)),
]
