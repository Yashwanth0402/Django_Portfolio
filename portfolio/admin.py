from django.contrib import admin
from .models import ResearchPaper


class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_abstract', 'display_file_link')
    list_display_links = ('title',)  # Make title clickable

    def display_abstract(self, obj):
        return obj.abstract[:50] + '...' if len(obj.abstract) > 50 else obj.abstract
    display_abstract.short_description = 'Abstract'

    def display_file_link(self, obj):
        return f'<a href="{obj.file.url}">View PDF</a>'
    display_file_link.allow_tags = True
    display_file_link.short_description = 'PDF File'


admin.site.register(ResearchPaper, ResearchPaperAdmin)
