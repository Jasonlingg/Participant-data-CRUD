from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.ParticipantList.as_view(), name='participant-list'),
]
