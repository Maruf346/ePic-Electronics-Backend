from django.urls import path
from .views import TutorialListView

urlpatterns = [
    path("", TutorialListView.as_view(), name="tutorial-list"),
]