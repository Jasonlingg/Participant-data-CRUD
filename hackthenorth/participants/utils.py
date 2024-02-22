from django.db.models import Count
from .models import Skill

def get_skills_with_frequency(min_frequency=None, max_frequency=None):
    # Start query to count the number of participants for each skill using ORM
    query = Skill.objects.annotate(frequency=Count('participantskill')).order_by('skill')
    
    # fiter based on the provided min_frequency and max_frequency, bounds are [x] interval
    if min_frequency:
        query = query.filter(frequency__gte=min_frequency)
    if max_frequency:
        query = query.filter(frequency__lte=max_frequency)
    
    return query