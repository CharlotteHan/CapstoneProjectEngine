from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project

# Create your views here.
def index(request):
    oldest_project_list = Project.objects.order_by('-id')[:20]
    template = loader.get_template('index.html')
    context = {
        'oldest_project_list': oldest_project_list,    
    }
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
    try:
        project = Project.objects.get(pk = project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'detail.html', {'project': project,}) 

def modify(request, project_id):
    return HttpResponse("You're changing project %s." % project_id)

def create(request):
    return HttpResponse("You're creating project.")
