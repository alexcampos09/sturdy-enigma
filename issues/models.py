# Django
from django.db import models

# Local
from profiles.models import Profile


class Issue(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
	title = models.CharField(max_length=120, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	# Meta
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def upvotes(self):
		return self.issueupvote_set.count()

	def get_absolute_url(self):
		return f"/issues/{self.pk}"

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'issues'

class IssueUpvote(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
	# Meta
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.profile}"

	class Meta:
		db_table = 'issue_upvote'

class Solution(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	title = models.CharField(max_length=120, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	# Meta
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def upvotes(self):
		return self.solutionupvote_set.count()

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'solutions'

class SolutionUpvote(models.Model):
	solution = models.ForeignKey(Issue, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
	# Meta
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.profile}"

	class Meta:
		db_table = 'solution_upvote'
