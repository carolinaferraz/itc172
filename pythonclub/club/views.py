from django.shortcuts import *
from .models import *


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