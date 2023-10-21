from django.test import TestCase
from persons.models import Person
from persons.serializers import PersonSerializer
from teams.models import Team


class TPersonSerializerTestCase(TestCase):
    def test_person_serializer_serializes_data(self):
        name = "test team"
        team = Team.objects.create(name=name)

        first_name = "test name"
        surname = "test surname"
        email = "test_email12@gmai.com"
        person1 = Person.objects.create(
            first_name=first_name, last_name=surname, email=email, team=team
        )

        first_name = "test name1"
        surname = "test surname1"
        email = "test_email22@gmai.com"
        person2 = Person.objects.create(
            first_name=first_name, last_name=surname, email=email, team=team
        )

        serializer_data = PersonSerializer([person1, person2], many=True).data
        self.assertTrue(serializer_data)
