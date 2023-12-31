from rest_framework.viewsets import ModelViewSet
from .models import Team
from .serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
