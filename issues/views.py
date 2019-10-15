# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Local
from issues.models import Issue, Solution
from issues.forms import IssueForm, SolutionForm


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'

    def get_queryset(self):
        original_queryset = super().get_queryset()
        return original_queryset.order_by('-upvotes')

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context['solutions'] = object.solution_set.all().order_by('-upvotes')
        context['form'] = SolutionForm()
        return context

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = "issues/issue_create.html"

    def form_valid(self, form):
        if form.is_valid():
            object = form.save(commit=False)
            object.profile = self.request.user.profile
            object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk' : self.object.pk})

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issues/issue_create.html"

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk' : self.object.pk})
