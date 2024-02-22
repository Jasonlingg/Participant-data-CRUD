from rest_framework import serializers
from .models import Participant, Skill, ParticipantSkill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill']

class ParticipantSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)  

    class Meta:
        model = ParticipantSkill
        fields = ['skill', 'rating']

class ParticipantSerializer(serializers.ModelSerializer):
    # custom serialized data (skills)
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Participant
        fields = ['id', 'name', 'company', 'email', 'phone', 'skills']

    # getting skills
    def get_skills(self, obj):
        # gets for this participant 
        participant_skills = ParticipantSkill.objects.filter(participant=obj)
        return [{'skill': ps.skill.skill, 'rating': ps.rating} for ps in participant_skills] # dictionary

    # for the update endpoint to handle updating information
    def update(self, instance, validated_data):
        skills_data = self.context['request'].data.get('skills', None)
        if skills_data is not None:
            # Assuming a PATCH request may not always contain skills and only update if skils exist
            existing_skills = {ps.skill.skill: ps for ps in ParticipantSkill.objects.filter(participant=instance)}
            for skill_data in skills_data:
                skill_name = skill_data.get('skill')
                rating = skill_data.get('rating')
                if skill_name in existing_skills:
                    # Update the RATING if the skill already exists doesnt create new or replace skills
                    existing_skill = existing_skills[skill_name]
                    existing_skill.rating = rating
                    existing_skill.save()
                else:
                    # Create a new ParticipantSkill if the skill does not exist for that person
                    skill, _ = Skill.objects.get_or_create(skill=skill_name)
                    ParticipantSkill.objects.create(participant=instance, skill=skill, rating=rating)
        return super().update(instance, validated_data)