from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.contrib.auth.models import User

from .models import Project
from .forms import ProjectForm, EOIForm, AllocateForm
from accounts.models import Group

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
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'detail.html', {'project': project}) 

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
            project.member=None
            project.save()
            return HttpResponseRedirect('/projects/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()
    return render(request, 'create.html', {'form': form}) 
    
def delete(request, project_id):
    Project.objects.get(pk=project_id).delete()
    return HttpResponseRedirect('/projects/')

def myprojects(request):
    oldest_project_list = Project.objects.filter(sponsor_id = request.user.profile)
    template = loader.get_template('index.html')
    context = {
        'oldest_project_list': oldest_project_list,    
    }
    return HttpResponse(template.render(context, request))

def myproject(request):
    group = Group.objects.filter(member = request.user.profile)
    if group.exists():
        if group.first().is_allocated != False:
            project = Project.objects.get(member = group.first())
            return render(request, 'detail.html', {'project': project}) 
    return render(request, 'myprojectblank.html',{})

def eoi(request):
 # if this is a POST request we need to process the form data
    myprofile = request.user.profile
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EOIForm(request.POST)
        students = []
        if form.is_valid():
            try:
                student1 = User.objects.get(username = form.cleaned_data['group_member1'])
                student2 = User.objects.get(username = form.cleaned_data['group_member2'])
                students.append(student1.profile)
                students.append(student2.profile)
                if form.cleaned_data['group_member3']:
                    student3 = User.objects.get(username = form.cleaned_data['group_member3'])
                    students.append(student3.profile)
            except User.DoesNotExist:
                raise Http404("Wrong group member id")
            # delete previous group information if the user has a group
            if Group.objects.filter(member = myprofile).exists():
                mygroup = Group.objects.filter(member = myprofile)
                mygroup.delete()
            mygroup = Group.objects.create()
            mygroup.member.add(myprofile)
            mygroup.save()
            form = EOIForm(request.POST, instance=Group.objects.filter(member = myprofile).first())
            mygroup = form.save(commit=False)
            for i in students:
                # Remove duplicate groups for group members
                if Group.objects.filter(member = i).exists():
                    tmp = Group.objects.filter(member = i)
                    tmp.delete()
                mygroup.member.add(i)
            mygroup.save()
            return HttpResponseRedirect('/projects/eoi_submitted/')
    else:
        form = EOIForm()
    return render(request, 'eoi.html', {'form': form}) 

def eoi_details(request):
    if Group.objects.filter(member = request.user.profile).exists():
        group = Group.objects.filter(member=request.user.profile).first()
        projects = []
        projects.append(group.choice1)
        projects.append(group.choice2)
        projects.append(group.choice3)
        return render(request, 'eoi_details.html',{'projects': projects, 'team_members': group.member.all()})
    else:
        return render(request, 'eoi_details.html',{})

def eoi_submitted(request):
    return render(request, 'eoi_submitted.html',{})

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
 # if this is a POST request we need to process the form data
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AllocateForm(request.POST, instance=project)
        if project.member != None:
            project.member.is_allocated=False
            project.member.save()
        if form.is_valid():
            project = form.save(commit=False)
            if project.member == None:
                project.is_allocated=False
            else:
                project.is_allocated=True
                project.member.is_allocated = True
                project.member.save()
            project.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = AllocateForm(instance=project)
        form.fields["member"].queryset = Group.objects.filter(choice1 = project, is_allocated=False) | Group.objects.filter(choice2 = project, is_allocated=False) | Group.objects.filter(choice3 = project, is_allocated=False)
    return render(request, 'modify.html', {'form': form,'project': project}) 
