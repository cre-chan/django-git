from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
import os


# Create your views here.

def create_repo(repo_name):
    os.system("mkdir /tmp/git/{0}.git&&git init --bare /tmp/git/{0}.git".format(repo_name))

def index(request):
    return render(request,'managesys/index.html',{})

def create(request):
    return render(request,'managesys/create.html',{})

def instructions(request):
    repo_name=request.POST['repo_name']
    create_repo(repo_name)
    return render(request,'managesys/instruction.html',{"repo_name":repo_name})