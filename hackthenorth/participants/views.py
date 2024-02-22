from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Participant, Skill
from .serializers import ParticipantSerializer

# Endpoint for all users
class ParticipantList(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
