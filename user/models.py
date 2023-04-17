from django.db import models
# from datetime import datetime
# # Create your models here.

# class project(models.Model):

#     name = models.CharField(max_length=20)
#     create_date = models.DateTimeField(auto_now_add=True)
#     due_date = models.DateTimeField(default=datetime.now)
#     project_code = models.CharField(max_length=20)
#     details = models.CharField(max_length=200)
#     team = models.CharField(max_length=200)
#     def __str__(self):
#         return self.details

# class to_do(models.Model):
#     text = models.CharField(max_length=20, null=True)
#     #project = models.ForeignKey(project, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     create_date = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateTimeField(default=datetime.now)
#     due_date = models.DateTimeField(default=datetime.now)
#     project_code = models.CharField(max_length=20)
#     details = models.TextField()

#     def __str__(self):
#         return self.text[:60] + "..."

# class in_progress(models.Model):
#     text = models.CharField(max_length=20, null=True)
#     #project = models.ForeignKey(project, on_delete=models.CASCADE)
#     name = models.ForeignKey(to_do, on_delete=models.CASCADE)
#     create_date = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateTimeField(default=datetime.now)
#     due_date = models.DateTimeField(default=datetime.now)
#     project_code = models.CharField(max_length=20)
#     details = models.TextField()
#     def __str__(self):
#         return self.text

# class done(models.Model):
#     text = models.CharField(max_length=20, null=True)
#     #project = models.ForeignKey(project, on_delete=models.CASCADE)
#     #name = models.ForeignKey(to_do, on_delete=models.CASCADE)

#     create_date = models.DateTimeField(auto_now_add=True)
#     start_date = models.DateTimeField(default=datetime.now)
#     due_date = models.DateTimeField(default=datetime.now)

#     project_code = models.CharField(max_length=20)
#     details = models.TextField()
#     def __str__(self):
#         return self.text




# # Users information
# class team(models.Model):
#     firstname = models.CharField(max_length=20)
#     lastname = models.CharField(max_length=20)
#     email = models.CharField(max_length=50)
#     position = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)

# class wiki(models.Model):
#     file = models.FileField(upload_to='wikis')

# class resource(models.Model):
#     resource = models.FileField(upload_to='resources')


# from django.contrib import admin
# admin.site.register(to_do)
# admin.site.register(in_progress)
# admin.site.register(done)
# admin.site.register(project)
# admin.site.register(team)
# admin.site.register(wiki)
# admin.site.register(resource)
