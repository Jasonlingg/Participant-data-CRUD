from django.contrib import admin
from .models import Participant, ParticipantSkill, Skill

admin.site.register(Participant)
admin.site.register(ParticipantSkill)
admin.site.register(Skill)