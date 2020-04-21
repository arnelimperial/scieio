from django.urls import path, include
from rest_framework import routers
from scieio.dna_synthesizers import views

router = routers.DefaultRouter()
router.register('list', views.DNASynthesizerViewSet)

app_name = "dna_synthesizers"
urlpatterns = [
    path('', include(router.urls)),
]
