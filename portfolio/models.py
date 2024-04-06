from django.db import models
from django.utils import timezone

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField(default='')  # Provide a default value
    abstract = models.TextField()
    file = models.FileField(upload_to='research_papers/', default='')

    def __str__(self):
        return self.title
