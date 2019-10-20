# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Local
from issues.models import Issue, IssueUpvote, Solution, SolutionUpvote
from issues.forms import IssueForm, SolutionForm


class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'

    def get_queryset(self):
        original_queryset = super().get_queryset()
        queryset = original_queryset.annotate(upvotes=Count('issueupvote')).order_by('-upvotes')
        return queryset

class IssueGetDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = self.object
        context['solutions'] = issue.solution_set.all().order_by()
        context['form'] = SolutionForm()
        casted = issue.issueupvote_set.filter(profile=self.request.user.profile)
        context['casted'] = True if casted else False
        return context

class SolutionPostCreateView(LoginRequiredMixin, CreateView):
    model = Solution
    form_class = SolutionForm
    template_name = 'issues/issue_detail.html'

    def form_valid(self, form):
        if form.is_valid():
            pk = self.request.path.split('/')[-1]
            solution = form.save(commit=False)
            solution.issue_id = pk
            solution.save()
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
            profile = self.request.user.profile
            issue = form.save(commit=False)
            issue.profile = profile
            issue.save()
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
        profile = self.request.user.profile
        issue = self.get_object()
        casted = issue.issueupvote_set.filter(profile=profile)
        if casted:
            return HttpResponse()
        IssueUpvote(issue=issue, profile=profile).save()
        data = {"upvotes": issue.upvotes()}
        return JsonResponse(data=data)

class SolutionUpvoteView(LoginRequiredMixin, UpdateView):
    model = Solution

    def post(self, request, *args, **kwargs):
        profile = self.request.user.profile
        solution = self.get_object()
        casted = solution.solutionupvote_set.filter(profile=profile)
        if casted:
            return HttpResponse()
        SolutionUpvote(solution=solution, profile=profile).save()
        data = {"upvotes": solution.upvotes()}
        return JsonResponse(data=data)
