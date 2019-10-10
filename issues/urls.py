# Django
from django.urls import path

# Local
from issues.views import *

urlpatterns = [
    path(r'', IssueListView.as_view(), name='issues'),
    path('<int:pk>', IssueDetailView.as_view(), name='issue-detail'),
    path('<int:pk>/update', IssueUpdateView.as_view(), name='issue-update'),
    path('create/', IssueCreateView.as_view(), name='issue-create'),
]
