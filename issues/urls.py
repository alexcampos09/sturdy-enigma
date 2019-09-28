# Django
from django.urls import path

# Local
from issues.views import *

urlpatterns = [
    path(r'', IssueListView.as_view(), name='issue'),
    path('<int:pk>', IssueDetailView.as_view(), name='issue-detail'),
]