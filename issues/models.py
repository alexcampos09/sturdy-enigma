from django.db import models


class Issue(models.Model):
	name = models.CharField(max_length=120, help_text='Issue', blank=False, null=False)
	description = models.TextField(help_text="What's wrong?", blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return f"/issues/{self.pk}"

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'issues'

