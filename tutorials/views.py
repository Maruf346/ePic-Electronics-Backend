from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Tutorial
from .serializers import TutorialSerializer


class TutorialListView(generics.ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = [AllowAny]