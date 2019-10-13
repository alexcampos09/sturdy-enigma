# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

# Local
from profiles.models import Profile
from profiles.forms import ProfileForm


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/profile_update.html"

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'pk' : self.object.pk})
