# Django
from django.forms import ModelForm

# Local
from issues.models import Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description']
