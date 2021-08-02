from django import http
from django.shortcuts import redirect, render
from task.models import tododata
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    posts=tododata()
    sucess=False
    if request.method=="POST":
        posts.name= request.POST.get('textname','defulat')
        posts.desc= request.POST.get('textdesc','defulat')
        posts.save()
        sucess=True
        
        return HttpResponse("data have submated")
    else:
        return render(request,'index.html')

def show(request):
  
        
      today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
      alldata=tododata.objects.all()
    
      parms={'items':alldata,'time':today}
      return render(request, 'show.html',parms)
    

def delete(request,id):
    deldata=tododata.objects.get(id=id)
    deldata.delete()
    return redirect('/show')
def edit(request,id):
    editdata=tododata.objects.get(id=id) 
    return render(request,'edit.html',{'editdata':editdata})   

def updates(request,id):
  
    user=tododata.objects.get(id=id)
    if request.method=="POST":
        user.name=request.POST.get('textname','defulat')
        user.desc=request.POST.get('textdesc','defulat')
        user.save()
        return redirect('/show')
    else:
        return HttpResponse("error in your data")    