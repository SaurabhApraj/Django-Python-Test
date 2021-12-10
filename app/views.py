from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from .forms import ClientReg
from .forms import UserReg
from .models import Client, Project
# Create your views here.
def home(request):
    if request.method == "POST":
        user = request.POST['user_name']
        password = request.POST['user_password']

        user = auth.authenticate(user_name = user,user_password = password)

        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                auth.login(request, user)
        else:
            print("Invalid")
            return redirect('/')
    else:
        pass
    return render(request, "app/index.html")

def show_client(request):
    client = Client.objects.all()
    return render(request, "app/clientinfo.html" ,{'client':client})

def delete_data(request,id):
    if request.method == "POST":
        user = Client.objects.get(pk=id)
        user.delete()
    return HttpResponseRedirect('/client')

def update_data(request,id):
    if request.method == "POST":
        usr = Client.objects.get(pk=id)
        fm = ClientReg(request.POST, instance=usr)
        if fm.is_valid():
            fm.save()
    else:
        pi = Client.objects.get(pk=id)
        fm = ClientReg(instance=pi)
    return render(request, "app/updateclient.html", {'form':fm})

def user_project_allot(request,id):
    if User.is_authenticated():
        # print(User.id)
        pro = Project.objects.get(pk=id)
    return render(request, "app/userprojectallot.html" ,{'pro':pro})