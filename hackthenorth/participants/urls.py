from django.urls import path
from .views import ParticipantList, ParticipantDetail, ParticipantUpdate, skills_view

urlpatterns = [
    path('users/', ParticipantList.as_view(), name='participant-list'),
    path('users/<int:pk>/', ParticipantDetail.as_view(), name='participant-detail'),
    path('users/<int:pk>/update/', ParticipantUpdate.as_view(), name='participant-update'),
    path('skills/', skills_view, name='skills-view'),
]