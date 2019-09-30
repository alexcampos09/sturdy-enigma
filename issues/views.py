# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

# Local
# from issues.forms import IssueForm
from issues.models import *


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'
    
