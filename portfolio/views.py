from .forms import ResearchPaperForm
from django.http import FileResponse

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render
from .models import ResearchPaper


def research_papers(request):
    papers = ResearchPaper.objects.all()
    return render(request, 'research.html', {'papers': papers})


def download_paper(request, paper_id):
    paper = ResearchPaper.objects.get(pk=paper_id)
    # Assuming 'file' is the name of the FileField in your ResearchPaper model
    file_path = paper.file.path
    return FileResponse(open(file_path, 'rb'))