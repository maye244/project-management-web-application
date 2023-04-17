from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.views.decorators.http import require_http_methods
# Create your views here.

# for forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Todo, Progress, Done
from .forms import ProjectForm, TodoForm, ProgressForm, DoneForm, dragTodoForm
from .models import Team, wiki, resource
from .forms import ResourceForm
from django.db.models import Case, When, Count
from django.db.models import Q
# gantt chart
# import plotly.express as px
# import pandas as pd
import json
def index(request):
    # Todo list homepage
    return render(request, 'todo_lists/index.html')


def projects(request):
    # show all projects

    projects = Project.objects.order_by('project_code')
    context = {'projects': projects}
    return render(request, 'todo_lists/projects.html', context)


def project(request, project_id):
    
    project = Project.objects.get(id=project_id)
    
    todos = project.todo_set.filter(status='to_do').order_by('-project_code')
    progresses = project.todo_set.filter(status='in_progress').order_by('-project_code')
    dones = project.todo_set.filter(status='done').order_by('-project_code')
    context = {'project': project, 'todos': todos, 'progresses': progresses, 'dones': dones}
    return render(request, 'todo_lists/project.html', context)

# def task(request, todo_id):
    
#     todos = Todo.objects.get(id=todo_id)
    
#     project = todos.project
    
#     context = {'project': project, 'todos': todos}
#     return render(request, 'todo_lists/task_detail.html', context)

def teams(request):
    teams = Team.objects.order_by('name')
    context = {'teams':teams}
    return render(request, 'todo_lists/teams.html', context)

def team(request, team_id):
    
    team = Team.objects.get(id=team_id)
    
    todos = team.todo_set.filter(status='to_do').order_by('name')
    progresses = team.todo_set.filter(status='in_progress').order_by('name')
    dones = team.todo_set.filter(status='done').order_by('name')
    context = {'team': team, 'todos': todos, 'progresses': progresses, 'dones': dones}
    return render(request, 'todo_lists/team.html', context)

def project_progress(request, project_id):
    
    project = Project.objects.get(id=project_id)
    team = project.team_set.order_by('-project_code')
    context = {'project': project, 'team': team}
    return render(request, 'todo_lists/progress.html', context)

def assign(request):
    team = Team.objects.all()
    todos = Todo.objects.all().order_by('team')
    # progresses = team.todo_set.filter(status='in_progress')
    # dones = team.todo_set.filter(status='done')
    context = {'todos': todos, 'team': team}
    return render(request, 'todo_lists/assign.html', context)


def progress(request, pk):
    to = get_object_or_404(Todo, pk=pk)
    to.update_status()
    return redirect(reverse('todo_lists:project', kwargs={'project_id': to.project.pk}))


def drag(request, project_id):
    project = Project.objects.get(id=project_id)
    todo = Todo.objects.filter(status='to_do')
    progress = Todo.objects.filter(status='in_progress')
    done = Todo.objects.filter(status='done')
    context = {'todo', todo, 'progress', progress, 'done', done, 'project', project}
    return render(request, 'todo_lists/project.html', context)


def add_to_progress(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    # project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = dragTodoForm()
    else:
        form = dragTodoForm(request.POST)
        if form.is_valid():  
            Todo.objects.filter(id=todo_id).update(status='in_progress')
            new_progress = form.save(commit=False)
            new_progress.project = project
            new_progress.save()
                   
        # progress = Todo.objects.filter(status='in_progress')
    context = {'form', form, 'todo', todo}
    return render(request, 'todo_lists/new_progress.html', context)


def add_to_done(request, todo_id, project_id):
    todo = Todo.objects.get(id=todo_id)
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = dragTodoForm()
    else:
        form = dragTodoForm(request.POST)
        Todo.objects.filter(id=todo_id).update(status='done')
    context = {'form', form, 'todo', todo, 'project', project}
    return render(request, 'todo_lists/new_done.html', context)


# def drag_progress(request):
#     view = self.context['view']
#     todo_id = id
#     todo = Todo.objects.get(pk=todo_id)
#     copy_todo = todo.progress.all()

#     todo.id = None
#     todo.save()
#     for item in copy_todo:todo
#     item.save()
#     todo.progress.add(item)


def new_project(request):
    # add new project
    
    if request.method != 'POST':
        # if not submit then create a new form for user
        form = ProjectForm()
    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect(reverse('todo_lists:projects'))
# team', 'name', 'due_date', 'project_code', 'details
    context = {'form': form}
    return render(request, 'todo_lists/new_project.html', context)


def new_todo(request, project_id):
    # add a to do task for a project
    project = Project.objects.get(id=project_id)
    # team = Team.objects.all().values
    team = Team.objects.all().values('name')
    if request.method != 'POST':
        form = TodoForm()
    else:
        form = TodoForm(data=request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.project = project
            form.team = Team.objects.all().values('name')
            new_todo.save()
            return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
    context = {'project': project, 'form': form, 'team': team}
    return render(request, 'todo_lists/new_todo.html', context)


def new_progress(request, project_id):
    # add a in-progress for a project
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = ProgressForm()
    else:
        form = ProgressForm(data=request.POST)
        if form.is_valid():
            new_progress = form.save(commit=False)
            new_progress.project = project
            new_progress.save()
            return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
    context = {'project': project, 'form': form}
    return render(request, 'todo_lists/new_progress.html', context)


def new_done(request, project_id):
    # add done tasks for a project
    project = Project.objects.get(id=project_id)
    
    if request.method != 'POST':
        form = DoneForm()
    else:
        form = DoneForm(data=request.POST)
        if form.is_valid():
            new_done = form.save(commit=False)
            new_done.project = project
            new_done.save()
            return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
    context = {'project': project, 'form': form}
    return render(request, 'todo_lists/new_done.html', context)


def edit_todo(request, todo_id):
    # edit current todo task

        todo = Todo.objects.get(id=todo_id)
    
        project = todo.project

        if request.method != 'POST':
            # first time filled with current content
            form = TodoForm(instance=todo)
        else:
            form = TodoForm(instance=todo, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('todo_lists:project',
                                                    args=[project.id]))

        context = {'todo': todo, 'project': project, 'form': form}
        return render(request, 'todo_lists/edit_todo.html', context)


def edit_project(request, project_id):
    # edit current project

        project = Project.objects.get(id=project_id)
    

        if request.method != 'POST':
            # first time filled with current content
            form = ProjectForm(instance=project)
        else:
            form = ProjectForm(instance=project, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('todo_lists:projects'))

        context = {'project': project, 'form': form}
        return render(request, 'todo_lists/edit_project.html', context)


     
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    
    if request.method == "POST":
        todo.delete()
        return HttpResponseRedirect(reverse('todo_lists:projects'))

    context = {'todo': todo}
    return render(request, 'todo_lists/delete.html', context)


def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        project.delete()
        return HttpResponseRedirect(reverse('todo_lists:projects'))

    context = {'project': project}
    return render(request, 'todo_lists/delete_project.html', context)


def edit_progress(request, progress_id):
    # edit current in-progress task
    progress = Progress.objects.get(id=progress_id)
    project = progress.project

    if request.method != 'POST':
        # first time filled with current content
        form = ProgressForm(instance=progress)
    else:
        form = ProgressForm(instance=progress, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_lists:project',
                                                args=[project.id]))

    context = {'progress': progress, 'project': project, 'form': form}
    return render(request, 'todo_lists/edit_progress.html', context)



def visualisations(request):
    todo = Todo.objects.all()
    todo_count = todo.count()
    progress = Progress.objects.all()
    progress_count = progress.count()
    done = Done.objects.all()
    done_count = done.count()
   
    context = {'todo_count': todo_count, 'progress_count': progress_count, 'done_count': done_count}

    return render(request, 'todo_lists/progress.html', context)


def visualisation(request, project_id):
    
    project = Project.objects.get(id=project_id)
   
    counts_data = project.todo_set.aggregate(
        to_do_count=Count('id', filter=Q(status='to_do')),
        in_progress_count=Count('id', filter=Q(status='in_progress')),
        done_count=Count('id', filter=Q(status='done'))
        )
    team = project.team_set.order_by('-employeeID')


    # df = pd.DataFrame([
    #     dict(Task='todos', Start='2009-01-01', Finish='2009-02-28'),
    #     dict(Task='progresses', Start='2009-03-05', Finish='2009-04-15'),
    #     dict(Task='dones', Start='2009-02-20', Finish='2009-06-30')
    # ])

    # fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
    # fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    # fig.show()
    # period = []
    # for i in data:
    #     year = m['start_date'].strftime('%Y')
    #     month = m['start_date'].strftime('%m')
    #     day = m['start_date'].strftime('%d')
    #     check = 'new Date(%s, %s, %s)' % (year, month, day)
    #     period.append([str(m[selected_mode]),check,m['']])
    # start_date = Todo.objects.order_by('-due_date').values('start_date')
    # due_date = Todo.objects.order_by('-due_date').values('due_date')
    todos = project.todo_set.order_by('-project_code')


    return render(request, 'todo_lists/progress.html', {"counts_data":counts_data,'team':team,'todos':todos})





# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-wiki-page-xxxxxxxxxxxxxxxxxx
def wikiMain(request):
    return render(request, 'todo_lists/wiki.html')

def wiki1(request):
    mod = wiki.objects
    ob = mod.get(id=1)
    wiki1 = ob.file
    response = HttpResponse(wiki1)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki1)
    return response

def readwiki1(request):
    mod = wiki.objects
    ob = mod.get(id=1)
    wiki1 = ob.file
    response = HttpResponse(wiki1)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki1)
    return response

def wiki2(request):
    mod = wiki.objects
    ob = mod.get(id=2)
    wiki2 = ob.file
    response = HttpResponse(wiki2)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki2)
    return response

def readwiki2(request):
    mod = wiki.objects
    ob = mod.get(id=2)
    wiki2 = ob.file
    response = HttpResponse(wiki2)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki2)
    return response

def wiki3(request):
    mod = wiki.objects
    ob = mod.get(id=3)
    wiki3 = ob.file
    response = HttpResponse(wiki3)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki3)
    return response

def readwiki3(request):
    mod = wiki.objects
    ob = mod.get(id=3)
    wiki3 = ob.file
    response = HttpResponse(wiki3)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki3)
    return response

def wiki4(request):
    mod = wiki.objects
    ob = mod.get(id=4)
    wiki4 = ob.file
    response = HttpResponse(wiki4)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki4)
    return response

def readwiki4(request):
    mod = wiki.objects
    ob = mod.get(id=4)
    wiki4 = ob.file
    response = HttpResponse(wiki4)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki4)
    return response

def wiki5(request):
    mod = wiki.objects
    ob = mod.get(id=5)
    wiki5 = ob.file
    response = HttpResponse(wiki5)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki5)
    return response

def readwiki5(request):
    mod = wiki.objects
    ob = mod.get(id=5)
    wiki5 = ob.file
    response = HttpResponse(wiki5)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki5)
    return response

def wiki6(request):
    mod = wiki.objects
    ob = mod.get(id=6)
    wiki6 = ob.file
    response = HttpResponse(wiki6)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki6)
    return response

def readwiki6(request):
    mod = wiki.objects
    ob = mod.get(id=6)
    wiki6 = ob.file
    response = HttpResponse(wiki6)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki6)
    return response

def wiki7(request):
    mod = wiki.objects
    ob = mod.get(id=7)
    wiki7 = ob.file
    response = HttpResponse(wiki7)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki7)
    return response

def readwiki7(request):
    mod = wiki.objects
    ob = mod.get(id=7)
    wiki7 = ob.file
    response = HttpResponse(wiki7)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki7)
    return response

def wiki8(request):
    mod = wiki.objects
    ob = mod.get(id=8)
    wiki8 = ob.file
    response = HttpResponse(wiki8)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki8)
    return response

def readwiki8(request):
    mod = wiki.objects
    ob = mod.get(id=8)
    wiki8 = ob.file
    response = HttpResponse(wiki8)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki8)
    return response

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-resources-xxxxxxxxxxxxxxxxxx
def resourcepage(request):
    resource_list = resource.objects.all()
    return render(request, "todo_lists/resource.html", {'resource_list':resource_list} )

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def upload(request):
    if request.method == "POST":
        filename = request.FILES.get("myfiles")
        if filename is None:
            messages.error(request, "Please select a file")
            return HttpResponseRedirect(reverse('todo_lists:resourcepage'))
        else:
            newfile = resource.objects.create()
            newfile.resource = filename
            newfile.save()
            return HttpResponseRedirect(reverse('todo_lists:resourcepage'))
    return render(request, "todo_lists/resource.html", locals())

def checkresource(request,id):
    mod = resource.objects
    ob = mod.get(id = id)
    resourceid = ob.resource
    response = HttpResponse(resourceid)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(resourceid)
    return response

def downloadresource(request,id):
    mod = resource.objects
    ob = mod.get(id = id)
    resourceid = ob.resource
    response = HttpResponse(resourceid)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resourceid)
    return response

def resource1(request):
    mod = resource.objects
    ob = mod.get(id=1)
    resource1 = ob.resource
    response = HttpResponse(resource1)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource1)
    return response

def readresource1(request):
    mod = resource.objects
    ob = mod.get(id=1)
    readresource1 = ob.resource
    response = HttpResponse(readresource1)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource1)
    return response

def resource2(request):
    mod = resource.objects
    ob = mod.get(id=2)
    resource2 = ob.resource
    response = HttpResponse(resource2)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource2)
    return response

def readresource2(request):
    mod = resource.objects
    ob = mod.get(id=2)
    readresource2 = ob.resource
    response = HttpResponse(readresource2)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource2)
    return response

def resource3(request):
    mod = resource.objects
    ob = mod.get(id=3)
    resource3 = ob.resource
    response = HttpResponse(resource3)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource3)
    return response

def readresource3(request):
    mod = resource.objects
    ob = mod.get(id=3)
    readresource3 = ob.resource
    response = HttpResponse(readresource3)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource3)
    return response

def resource4(request):
    mod = resource.objects
    ob = mod.get(id=4)
    resource4 = ob.resource
    response = HttpResponse(resource4)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource4)
    return response

def readresource4(request):
    mod = resource.objects
    ob = mod.get(id=4)
    readresource4 = ob.resource
    response = HttpResponse(readresource4)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource4)
    return response

def assignpage(request):
    teams1 = Team.objects.all()
    # projects1 = Project.objects.all()
    context = {'teams1':teams1}
    return render(request, "todo_lists/assign.html",context)

def assign2(request):
    a_team = request.POST.get('team')
    a_name = request.POST.get('project_name')
    obj = Project(team=a_team, name=a_name)
    obj.save()
    # return render(request, 'todo_lists/assign.html')
    return HttpResponseRedirect(reverse('todo_lists:assignpage'))

def searchref(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = 'Please enter what you want to search'
        return render(request, "todo_lists/resource.html", {'error_msg':error_msg})
    resource_list = resource.objects.filter(Q(resource=q))
    return render(request,"todo_lists/resource.html", {'error_msg':error_msg, 'resource_list':resource_list})

# def assignpage(request, project_id):
#     # add done tasks for a project
#     project = Project.objects.get(id=project_id)

#     if request.method != 'POST':
#         form = DoneForm()
#     else:
#         form = DoneForm(data=request.POST)
#         if form.is_valid():
#             new_done = form.save(commit=False)
#             new_done.project = project
#             new_done.save()
#             return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
#     context = {'project': project, 'form': form}
#     return render(request, 'todo_lists/new_done.html', context)