# Create model classes for the python club database. These should include:

# Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda

# Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text

# Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description

# Event which will have fields for event title, location, date, time, description and the user id of the member that posted it


from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#------------------------------------------------
# TECHAPP CODE FOR REFERENCE

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutestext=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingminutes
    
    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField()
    dateentered=models.DateField()
    userid=models.ManyToManyField(User)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'