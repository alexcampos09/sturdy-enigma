# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
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

class IssueGetDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context['solutions'] = object.solution_set.all().order_by('-upvotes')
        context['form'] = SolutionForm()
        return context

class SolutionPostCreateView(LoginRequiredMixin, CreateView):
    model = Solution
    form_class = SolutionForm
    template_name = 'issues/issue_detail.html'

    def form_valid(self, form):
        if form.is_valid():
            pk = self.request.path.split('/')[-1]
            object = form.save(commit=False)
            object.issue_id = pk
            object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk' : self.object.issue.pk})

class IssueDetailView(View):
    """IssueGetDetailView and SolutionPostCreateView above work together to compose this view"""

    def get(self, request, *args, **kwargs):
        view = IssueGetDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SolutionPostCreateView.as_view()
        return view(request, *args, **kwargs)

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

class IssueUpvoteView(LoginRequiredMixin, UpdateView):
    model = Issue

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        object.upvotes += 1
        object.save()
        return HttpResponse(status=200)
