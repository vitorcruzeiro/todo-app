from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from todo.api.serializers import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

