from django.db import models
import datetime

class Project(models.Model):
    
    name = models.CharField(max_length=20) 
    create_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    project_code = models.CharField(max_length=20)
    details = models.TextField()
    member = models.CharField(max_length=200)

    def __str__(self):
        return self.details


class Todo(models.Model):
    
    status_option = (
        ('to_do', 'to_do'),
        ('in_progress', 'in_progress'),
        ('done', 'done'),
    )
    status = models.CharField(max_length=20, choices=status_option, default='to_do')
    # todo_list's content
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    priority_level = models.IntegerField(default=1)
    project_code = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return self.details[:20]+"..."
        # return self.team['team'].queryset

    def update_status(self):
        if self.status == 'to_do':
            self.status = 'in_progress'
        elif self.status == 'in_progress':
            self.status = 'done'
        self.save()

    # def __init__(self):
        
    #     self.team['team'].queryset = Team.objects.all()


class Progress(models.Model):  
    text = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    name = models.ForeignKey(Todo, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True) 
    start_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    
    project_code = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return self.text


class Done(models.Model):
    text = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.ForeignKey(Todo, on_delete=models.CASCADE)
    # name = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    
    project_code = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return self.text


class Team(models.Model):
    name = models.CharField(max_length=20)
    employeeID = models.CharField(max_length=20)
    
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def toDict(self):
        return {'id':self.id, 'employeeID':self.employeeID, 'name':self.name,
        'email':self.email, 'position':self.position, 'password':self.password}
    


class wiki(models.Model):
    file = models.FileField(upload_to='wikis')

class resource(models.Model):
    resource = models.FileField(upload_to='resources')

from django.contrib import admin
admin.site.register(Todo)
admin.site.register(Progress)
admin.site.register(Done)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(wiki)
admin.site.register(resource)
