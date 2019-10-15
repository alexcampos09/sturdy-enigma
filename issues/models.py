# Django
from django.db import models

# Local
from profiles.models import Profile


class Issue(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
	title = models.CharField(max_length=120, help_text='Issue', blank=False, null=False)
	body = models.TextField(help_text="What's wrong?", blank=False, null=False)
	upvotes = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return f"/issues/{self.pk}"

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'issues'

class Solution(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	title = models.CharField(max_length=120, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	upvotes = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'solutions'
