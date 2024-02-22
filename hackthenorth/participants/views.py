from django.shortcuts import render
from rest_framework import generics
from .models import Participant
from .serializers import ParticipantSerializer
from django.http import JsonResponse
from .utils import get_skills_with_frequency  

# Endpoint for all users
class ParticipantList(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

# Endpoint for user details
class ParticipantDetail(generics.RetrieveAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

# Endpoint for updating user data
class ParticipantUpdate(generics.UpdateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

# Correct function based view function to query skills
def skills_view(request):
    # get min_frequency and max_frequency from query parameters
    min_frequency = request.GET.get('min_frequency')
    max_frequency = request.GET.get('max_frequency')
    
    # Convert query parameters to integers if not None
    min_frequency = int(min_frequency) if min_frequency is not None else None
    max_frequency = int(max_frequency) if max_frequency is not None else None

    # Get the filtered skills with frequencies from our utils.py
    skills = get_skills_with_frequency(min_frequency, max_frequency)

    # Prepare the data to be returned as JSON
    data = [{'name': skill.skill, 'frequency': skill.frequency} for skill in skills]
    return JsonResponse(data, safe=False)
