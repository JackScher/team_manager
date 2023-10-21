from django.test import TestCase
from persons.models import Person
from teams.models import Team


class PersonModelTestCase(TestCase):
    def setUp(self) -> None:
        team_name = "test team"
        team = Team.objects.create(name=team_name)
        first_name = "test name"
        surname = "test surname"
        email = "test_email12@gmai.com"
        Person.objects.create(
            first_name=first_name, last_name=surname, email=email, team=team
        )

    def test_model_exists(self):
        persons = Person.objects.count()
        self.assertEqual(persons, 1)

    def test_model_has_string_representation(self):
        person = Person.objects.first()
        self.assertEqual(
            str(person), f"{person.id}: {person.first_name} {person.last_name}"
        )
