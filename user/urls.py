# users urls
from django.urls import path, include
from user.views import index
urlpatterns = [
    path('', index.index, name='index'),
    path('login/', index.login, name='login'),
    path('register/', index.register, name='register'),
    path('logout/', index.logout, name='logout'),
]
