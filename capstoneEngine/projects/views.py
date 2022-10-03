from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User

from .models import Project
from .forms import ProjectForm
from .forms import EOIForm

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
 # if this is a POST request we need to process the form data
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'modify.html', {'form': form,'project': project}) 

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

def eoi(request):
 # if this is a POST request we need to process the form data
    profile = request.user.profile
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EOIForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = EOIForm(instance=profile)
    return render(request, 'eoi.html', {'form': form}) 

def project_list(request):
    return render(request, 'project_list_choice.html',{})

def allocated(request):
    oldest_project_list = Project.objects.filter(is_allocated = True).reverse()
    template = loader.get_template('index.html')
    context = {
        'oldest_project_list': oldest_project_list,    
    }
    return HttpResponse(template.render(context, request))

def unallocated(request):
    oldest_project_list = Project.objects.filter(is_allocated = False).reverse()
    template = loader.get_template('index.html')
    context = {
        'oldest_project_list': oldest_project_list,    
    }
    return HttpResponse(template.render(context, request))

def allocate(request, project_id):
    return HttpResponse("You're browsing allocate")

def eoi_details(request):
    if request.user.profile.choice1 == None:
        return render(request, 'eoi_details.html',{})
    else:
        projects = []
        project1 = Project.objects.get(pk = request.user.profile.choice1)
        project2 = Project.objects.get(pk = request.user.profile.choice2)
        project3 = Project.objects.get(pk = request.user.profile.choice3)
        projects.append(project1)
        projects.append(project2)
        projects.append(project3)
        return render(request, 'eoi_details.html',{'projects': projects, 'project2': project2, 'project3': project3})
