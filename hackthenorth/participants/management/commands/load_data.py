import json
from django.core.management.base import BaseCommand
from participants.models import Participant, Skill, ParticipantSkill
from django.db import transaction

# BaseCommand to load the data into the database
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with transaction.atomic():
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                for user in data:
                    participant, created = Participant.objects.get_or_create(
                        # Use email as the unique identifier bc in theory it should be diff for all
                        email=user['email'],  
                        defaults={
                            'name': user['name'],
                            'company': user['company'],
                            'phone': user['phone']
                        }
                    )

                    for skill in user['skills']:
                        skill_obj, _ = Skill.objects.get_or_create(skill=skill['skill'])

                        # Check if the ParticipantSkill relationship already exists, and update or create it
                        participant_skill, created = ParticipantSkill.objects.get_or_create(
                            participant=participant,
                            skill=skill_obj,
                            defaults={'rating': skill['rating']}  # This sets the rating if creating a new entry
                        )

                        # If the ParticipantSkill already exists (not created), update the rating
                        if not created:
                            participant_skill.rating = skill['rating']
                            participant_skill.save()

            self.stdout.write(self.style.SUCCESS('Successfully loaded user data into the database'))