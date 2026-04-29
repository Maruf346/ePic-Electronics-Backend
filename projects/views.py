from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Project
from .serializers import ProjectSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]