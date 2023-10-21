from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    persons = models.ManyToManyField("persons.Person")

    @property
    def related_persons(self):
        return [str(person) for person in self.persons.all()]

    def __str__(self):
        return self.name
