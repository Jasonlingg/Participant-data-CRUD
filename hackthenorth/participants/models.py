from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Skill(models.Model):
    skill = models.CharField(max_length=255)
    participants = models.ManyToManyField(Participant, through='ParticipantSkill')

    def __str__(self):
        return self.skill

class ParticipantSkill(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = (('participant', 'skill'),)

    def __str__(self):
        return f"{self.participant.name}'s skill {self.skill.skill} rating: {self.rating}"