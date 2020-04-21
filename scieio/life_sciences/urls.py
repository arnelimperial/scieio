from django.urls import path, include
from rest_framework import routers
from scieio.life_sciences import views

router = routers.DefaultRouter()
router.register('categories', views.LifeScienceViewSet)

app_name = "life_sciences"
urlpatterns = [
    path('', include(router.urls)),
]
