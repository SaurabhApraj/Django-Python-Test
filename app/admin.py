from django.contrib import admin
from .models import User
from .models import Client
from .models import Project

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Project)