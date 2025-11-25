from django.urls import path
from django.views.generic.base import RedirectView

from .views import SubjectListView, VotingView

app_name = "subjects"

urlpatterns = [
    path("", RedirectView.as_view(url="/subjects/", permanent=True), name="home"),
    path("subjects/", SubjectListView.as_view(), name="subjects_list"),
    path("subjects/<int:subject_id>/vote/", VotingView.as_view(), name="subject_vote"),
]
