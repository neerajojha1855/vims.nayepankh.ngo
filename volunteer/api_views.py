from rest_framework import viewsets
from .models import Volunteer, Task
from .serializers import VolunteerSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]