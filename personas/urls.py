from django.urls import path
from personas.views import (
    personaCreateView,
    personasAnotherCreateView,
    personasDeleteView,
    personasListView,
    personasShowObject,
)

app_name = 'personas'
urlpatterns = [
    path('add/', personaCreateView, name='adding'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID/delete', personasDeleteView, name='deleting'),
    path('', personasListView, name='listing'),
]
