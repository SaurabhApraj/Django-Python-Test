from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user_name

class Client(models.Model):
    client_name = models.CharField(max_length=20)
    client_created_at = models.DateTimeField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_title = models.CharField(max_length=20)
    project_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title