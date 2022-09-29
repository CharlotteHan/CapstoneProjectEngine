from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User

from .models import Project
from .forms import ProjectForm

# Create your views here.
def index(request):
    oldest_project_list = Project.objects.order_by('-id').reverse()
    template = loader.get_template('index.html')
    context = {
        'oldest_project_list': oldest_project_list,    
    }
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
    try:
        project = Project.objects.get(pk = project_id)
        creator = User.objects.get(username = project.sponsor_id.user)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'detail.html', {'project': project, 'creator': creator}) 

def modify(request, project_id):
    return HttpResponse("You're changing project %s." % project_id)

def create(request):
 # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            project = form.save(commit=False)
            project.sponsor_id=user=request.user.profile
            project.is_allocated=False
            project.save()
            return HttpResponseRedirect('/projects/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()
    return render(request, 'create.html', {'form': form}) 

def myprojects(request):
    oldest_project_list = Project.objects.filter(sponsor_id = request.user.profile)
    template = loader.get_template('index.html')
    context = {
        'oldest_project_list': oldest_project_list,    
    }
    return HttpResponse(template.render(context, request))

def myproject(request):
    return HttpResponse("You're browsing your project")
