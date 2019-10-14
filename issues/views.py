# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Local
from issues.models import Issue
from issues.forms import IssueForm


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'

    def get_queryset(self):
        original_queryset = super().get_queryset()
        return original_queryset.order_by('-upvotes')

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = "issues/issue_create.html"

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk' : self.object.pk})

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issues/issue_create.html"

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk' : self.object.pk})
