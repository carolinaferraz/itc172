from django.test import TestCase
from .models import Theater, Movie
from .forms import TheaterForm, MovieForm
from django.contrib.auth.models import User


# your tests go here:

class TheaterTest(TestCase): 
    def test_string(self):
        ttr = Theater(name='theater name')
        self.assertEqual(str(ttr), ttr.name)

    def test_table(self):
        self.assertEqual(str(Theater._meta.db_table), 'theater')


class MovieTest(TestCase):
    def test_string(self):
        mov = Movie(title='movie title')
        self.assertEqual(str(mov), mov.title)

    def test_table(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')



#tests for form

class MovieForm_Test(TestCase):
    def test_typeform_minus_descript(self):
        form=MovieForm(data={'title': "movie title", 'description': " "})
        self.assertFalse(form.is_valid())

    def test_typeform_empty(self):
        form=MovieForm(data={'url': ""})
        self.assertFalse(form.is_valid())