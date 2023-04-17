# sub urls for todo_list


from django.urls import path

from . import views

app_name = 'todo_lists'
urlpatterns = [
    # homepage
    path('', views.projects, name='index'),
    # page that shows all projects
    path('projects/', views.projects, name='projects'),
    # details of a project
    path('projects/<int:project_id>/', views.project, name='project'),
    path('visual/<int:project_id>/', views.visualisation, name='visualisation'),
    # add a new project
    path('new_project/', views.new_project, name='new_project'),
    path('todoprogress/<slug:pk>/', views.progress, name='todoprogress'),
    path('teams/', views.teams, name='teams'),
    path('teams/<int:team_id>/', views.team, name='team'),


    # for creating new todo tasks by user
    path('new_todo/<int:project_id>/', views.new_todo, name='new_todo'),
    # for creating new todo tasks by user
    path('new_progress/<int:project_id>/', views.add_to_progress, name='new_progress'),
    # for creating new todo tasks by user
    path('new_done/<int:project_id>/', views.add_to_done, name='new_done'),
    
    # for editing current todo tasks
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    # for editing current in-progress tasks
    path('edit_progress/<int:progress_id>/', views.edit_progress, name='edit_progress'),
    path('progress/', views.visualisation, name='visualisation'),
    path('delete/<str:todo_id>/', views.delete_todo, name='delete_todo'),
    path('delete_project/<str:project_id>/', views.delete_project, name='delete_project'),
    path('edit_project/<str:project_id>/', views.edit_project, name='edit_project'),

    path('wiki', views.wikiMain, name='wikiMain'),
    path('wiki1', views.wiki1, name='wiki1'),
    path('readwiki1', views.readwiki1, name='readwiki1'),
    path('wiki2', views.wiki2, name='todo_lists_wiki2'),
    path('readwiki2', views.readwiki2, name='readwiki2'),
    path('wiki3', views.wiki3, name='wiki3'),
    path('readwiki3', views.readwiki3, name='readwiki3'),
    path('wiki4', views.wiki4, name='wiki4'),
    path('readwiki4', views.readwiki4, name='readwiki4'),
    path('wiki5', views.wiki5, name='wiki5'),
    path('readwiki5', views.readwiki5, name='readwiki5'),
    path('wiki6', views.wiki6, name='wiki6'),
    path('readwiki6', views.readwiki6, name='readwiki6'),
    path('wiki7', views.wiki7, name='wiki7'),
    path('readwiki7', views.readwiki7, name='readwiki7'),
    path('wiki8', views.wiki8, name='wiki8'),
    path('readwiki8', views.readwiki8, name='readwiki8'),



    path('resourcepage', views.resourcepage, name='resourcepage'),
    path('resource1', views.resource1, name='resource1'),
    path('readresource1', views.readresource1, name='readresource1'),
    path('resource2', views.resource2, name='resource2'),
    path('readresource2', views.readresource2, name='readresource2'),
    path('resource3', views.resource3, name='resource3'),
    path('readresource3', views.readresource3, name='readresource3'),
    path('resource4', views.resource4, name='resource4'),
    path('readresource4', views.readresource4, name='readresource4'),
    path('upload', views.upload, name='upload'),
    path('checkresource<id>', views.checkresource, name='checkresource'),
    path('downloadresource<id>', views.downloadresource, name='downloadresource'),
    path('searchref', views.searchref, name='searchref'),

    path('searchref', views.searchref, name='searchref'),
    path('assignpage/', views.assign, name='assign'),
    path('assign2', views.assign2, name='project_assign2'),
]
