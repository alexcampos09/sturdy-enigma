# Django
from django.forms import ModelForm

# Local
from profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']
