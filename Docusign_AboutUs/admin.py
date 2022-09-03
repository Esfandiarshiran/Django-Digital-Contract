from django.contrib import admin
from Docusign_AboutUs.models import TeamMembers


# admin.site.register(TeamMembers)

@admin.register(TeamMembers)
class AboutUSAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_title', 'email')
    list_filter = ('title', 'job_title', 'email')
    search_fields = ('title', 'job_title', 'email')
    ordering = ('title', 'job_title')
