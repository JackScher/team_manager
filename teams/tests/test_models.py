from django.test import TestCase
from teams.models import Team


class TeamModelTestCase(TestCase):
    def setUp(self) -> None:
        name = "test team"
        Team.objects.create(name=name)

    def test_model_exists(self):
        teams = Team.objects.count()
        self.assertEqual(teams, 1)

    def test_model_has_string_representation(self):
        team = Team.objects.first()
        self.assertEqual(str(team), team.name)
