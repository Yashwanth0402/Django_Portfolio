from django import forms
from .models import ResearchPaper

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['title', 'author', 'publication_date', 'abstract', 'file']
