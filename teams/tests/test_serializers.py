from django.test import TestCase
from teams.models import Team
from teams.serializers import TeamSerializer


class TeamSerializerTestCase(TestCase):
    def test_team_serializer_serializes_data(self):
        name1 = "test team"
        name2 = "test team 1"
        team1 = Team.objects.create(name=name1)
        team2 = Team.objects.create(name=name2)
        serializer_data = TeamSerializer([team1, team2], many=True).data
        self.assertTrue(serializer_data)
