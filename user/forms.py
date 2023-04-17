from django import forms
from django.forms import widgets
from todo_lists.models import Team, Project, resource, wiki, Todo, Progress, Done
# Create your form class

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), label='password', max_length=50)
    widgets = {password: forms.PasswordInput(),}

class RegisterForm(forms.Form):
    employeeID = forms.CharField(label='employee', max_length=20, required=True,
                                error_messages={'required':'Please fill in your employeeID'})
    name = forms.CharField(label='name', max_length=20, required=True,
                               error_messages={'required':'Please fill in your name'})
    email = forms.EmailField(label='email', max_length=50,
                             required=True,
                             error_messages={'required':'Please fill in your email adress','invalid':'Invalid email adress'})
    position = forms.CharField(label='position', max_length=50,
                              required=True,
                              error_messages={'required':'Please select your position'})
    password = forms.CharField(widget=forms.PasswordInput(), label='password', max_length=50,
                               required=True,
                               error_messages={'required':'Please fill in your password'})
    comfirmpw = forms.CharField(widget=forms.PasswordInput(), label='comfirmpw', max_length=50,
                                required=True,
                                error_messages={'required':'Please refill your password'})

# class ResourceForm(forms.Form):
#     resource = forms.FileField(label='resource', required=True, error_messages={'required':'Please select a file'})

# class ProjectForm(forms.ModelForm): 
#     class Meta:
#         model = Project
#         fields = ['team', 'name', 'due_date', 'project_code', 'details']
#         widgets = {
#                     'start_date': forms.SelectDateWidget(),
#                     'due_date': forms.SelectDateWidget(),
#         }

# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = [ 'text', 'name', 'start_date', 'due_date',
#                   'project_code', 'details']
#         # labels = {'project': '', 'create_date': ''}
#         widgets = {
#                     # 'project': forms.Textarea(attrs={'col': 100}),
#                     'start_date': forms.SelectDateWidget(),
#                     'due_date': forms.SelectDateWidget(),
#                     # 'resources': forms.FileInput()
#                 }

# class ProgressForm(forms.ModelForm):
#     class Meta:
#         model = Progress
#         fields = [ 'text', 'name', 'start_date', 'due_date',
#                   'project_code', 'details']

# class DoneForm(forms.ModelForm):
#     class Meta:
#         model = Done
#         fields = [ 'text', 'start_date', 'due_date',
#                   'project_code', 'details']
