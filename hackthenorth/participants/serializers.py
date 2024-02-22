from rest_framework import serializers
from .models import Participant, Skill, ParticipantSkill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill']

class ParticipantSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)  # Serialize the skill details

    class Meta:
        model = ParticipantSkill
        fields = ['skill', 'rating']

class ParticipantSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Participant
        fields = ['id', 'name', 'company', 'email', 'phone', 'skills']

    def get_skills(self, obj):
        participant_skills = ParticipantSkill.objects.filter(participant=obj)
        return [{'skill': ps.skill.skill, 'rating': ps.rating} for ps in participant_skills]

    def create(self, validated_data):
        skills_data = self.context['request'].data.get('skills', [])
        participant = Participant.objects.create(**validated_data)
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(skill=skill_data['skill'])
            ParticipantSkill.objects.create(participant=participant, skill=skill, rating=skill_data['rating'])
        return participant

    def update(self, instance, validated_data):
        skills_data = self.context['request'].data.get('skills', [])
        instance.skills.clear()  # Clear existing skills and their ratings
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(skill=skill_data['skill'])
            ParticipantSkill.objects.update_or_create(participant=instance, skill=skill, defaults={'rating': skill_data['rating']})
        return super().update(instance, validated_data)
