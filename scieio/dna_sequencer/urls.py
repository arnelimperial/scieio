from django.urls import path, include
from rest_framework import routers
from scieio.dna_sequencer import views

router = routers.DefaultRouter()
router.register('list', views.DNASequencerViewSet)

app_name = "dna_sequencer"
urlpatterns = [
    path('', include(router.urls)),
]
