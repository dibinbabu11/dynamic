from django.shortcuts import render
from .models import Featured,Dibi,Read,Instagram
from django .http import HttpResponse

# Create your views here.

def index(request):
    obj=Featured.objects.all()
    abc=Read.objects.all()
    new=Instagram.objects.all()
    return render(request,"index.html",{'result':obj , 'abcd':abc,'new':new})

def components(request):
    return render(request,"components.html")

def no(request):
    return render(request,"no-sidebar.html")

def components(request):
    return render(request,"components.html")

def single(request):
    return render(request,"single-post.html")
