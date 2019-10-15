# Django
from django.contrib import admin

# Local
from issues.models import Issue, Solution


class SolutionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "issue",
    ]

admin.site.register(Issue)
admin.site.register(Solution, SolutionAdmin)
