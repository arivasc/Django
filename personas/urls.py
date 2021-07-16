from django.urls import path
from personas.views import (
    personaCreateView,
    personasAnotherCreateView,
    personasDeleteView,
    personasListView,
    personasShowObject,
)
from .views import (
    PersonaCreateView,
    PersonaListView,
    PersonaDetailView,
    PersonaUpdateView,
)

app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name = 'persona-detail'),
    path('create/', PersonaCreateView.as_view(), name = 'persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name = 'persona-update'),
    path('add/', personaCreateView, name='adding'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID/delete', personasDeleteView, name='deleting'),
    path('', personasListView, name='listing'),
]
