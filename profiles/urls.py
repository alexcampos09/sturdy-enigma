# Django
from django.urls import path

# Local
from profiles.views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='profile-update'),
]
