from django.shortcuts import redirect, render
from django.urls import reverse
import re
from django.contrib import messages

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('ShopMiddleware')

    def __call__(self, request):
        path = request.path
        print('url:',path)

        #login or not
        urlist = ['/index','/login','/register','/logout']
        if re.match(r'^/todo_lists',path) and (path not in urlist):
            if 'stuff' not in request.session:
                return redirect(reverse('login'))
        if re.match(r'^/todo_lists/new_project',path):
            if 'stuff' in request.session:
                if request.session['stuff']['position'] != 'manager' :
                    message = "Only manager can add new projects!"
                    request.session['error']=message
                    return redirect('/todo_lists/projects/')

        #if re.match(r'^/todo_lists/new_todo/',path):
        #    if 'stuff' in request.session:
        #        if request.session['stuff']['position'] != 'manager' :
        #            message = "Only manager can assign tasks to team member"
        #            request.session['message']=message
        #            return redirect('/todo_lists/projects/1/')



        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
