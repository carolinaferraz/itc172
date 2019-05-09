from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event


# your tests go here:

class MeetingTest(TestCase): 
    def test_string(self):
        meet = Meeting(meetingtitle='team meeting 01')
        self.assertEqual(str(meet), meet.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def test_string(self):
        mtext = MeetingMinutes(minutestext='this is what happened')
        self.assertEqual(str(mtext), mtext.minutestext)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename='tutorial')
        self.assertEqual(str(type), type.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def test_string(self):
        title=Event(eventtitle='big event 01')
        self.assertEqual(str(title), title.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')