from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo_lists.models import Team
from user.forms import UserForm,RegisterForm

#from django.contirb.auth import logout

# Create your views here.
def index(request):
    '''home page'''
    return render(request,'user/Homepage.html')

def login(request):
    '''login page'''
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = 'Check your filling!'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                users= Team.objects.get(email=username)

                if users.password == password:
                    #uname = users.name
                    #newname = loginname.objects.get(id=1)
                    #newname.loginname = uname
                    #newname.save()
                    request.session['stuff'] = users.toDict()
                    request.session['error'] =""

                    return redirect('/todo_lists/')
                else:
                    message = "Invalid password!"
            except:
                message = "The user do not have an account！"
        return render(request, 'user/login.html', locals())

    login_form = UserForm()
    return render(request, 'user/login.html',locals())


# def register(request):
#     '''register page'''

#     if request.method == "POST":
#         register_form = RegisterForm(request.POST)
#         message = "Check you filling！"
#         if register_form.is_valid():
#             email = register_form.cleaned_data['email']
#             password1 = register_form.cleaned_data['password']
#             password2 = register_form.cleaned_data['comfirmpw']
#             firstname = register_form.cleaned_data['firstname']
#             lastname = register_form.cleaned_data['lastname']
#             position = register_form.cleaned_data['position']
#             if password1 != password2:
#                 message = "Different password!"
#                 return render(request, 'user/register.html', locals())
#             else:
#                 emailadress = Team.objects.filter(email=email)

#                 if emailadress:
#                     message = 'The user had an account already！'
#                     return render(request, 'user/register.html', locals())
#                 else:
#                     new_user = Team.objects.create()
#                     new_user.firstname = firstname
#                     new_user.lastname = lastname
#                     new_user.password = password1
#                     new_user.email = email
#                     new_user.position = position
#                     new_user.save()
#                     return redirect('/login/')
#         else:
#             print(register_form.errors)
#     register_form = Team()
#     return render(request, 'user/register.html', locals())

def register(request):
    '''register page'''

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Check you filling！"
        if register_form.is_valid():
            email = register_form.cleaned_data['email']
            password1 = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['comfirmpw']
            employee = register_form.cleaned_data['employeeID']
            name = register_form.cleaned_data['name']
            position = register_form.cleaned_data['position']
            try:
                new_user = Team.objects.get(employeeID=employee)

                if password1 != password2:
                    message = "Different password!"
                    return render(request, 'user/register.html', locals())
                else:
                    emailadress = Team.objects.filter(email=email)

                    if emailadress:
                        message = 'The user had an account already！'
                        return render(request, 'user/register.html', locals())
                    else:
                        #new_user = team.objects.get(firstname = firstname)
                        #new_user.firstname = firstname
                        new_user.name = name
                        new_user.password = password1
                        new_user.email = email
                        new_user.position = position
                        new_user.save()
                        return redirect('/login/')
            except:
                message = "You are not an employee of PNP company"
        else:
            print(register_form.errors)
    register_form = Team()
    return render(request, 'user/register.html', locals())


def logout(request):
    '''logout page'''
    del request.session['stuff']
    del request.session['error']
    return redirect('/login/')


def project(request):
    '''home page'''
    return render(request,'todo_lists/projects.html')
