from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

#resources 
def getresources(request):
    type_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'type_list' : type_list})

#meetings
def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/meetings.html' ,{'meetings_list' : meetings_list})

#meeting details
def getdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    mm=MeetingMinutes
    
    context={
        'meet': meet,
        'mm' : mm,
    }
    return render(request, 'club/meetingsdetails.html', context=context)

@login_required
#add meeting
def newmeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'club/newmeeting.html', {'form': form})

@login_required
#add resource
def newresource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'club/newresource.html', {'form': form})

#login/logout
def loginmsg(request):
    return render(request, 'club/loginmsg.html')

def logoutmsg(request):
    return render(request, 'club/logoutmsg.html')
