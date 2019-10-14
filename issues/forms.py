# Django
from django.forms import ModelForm

# Local
from issues.models import Issue, Solution


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'body']

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['title', 'body']
