from django.test import TestCase
from .models import Theater, Movie
from .forms import TheaterForm, MovieForm
from django.contrib.auth.models import User


# your tests go here:

# class TheaterTest(TestCase): 
#     def test_string(self):
#         ttr = Theater(name='theater name')
#         self.assertEqual(str(ttr), ttr.name)

#     def test_table(self):
#         self.assertEqual(str(Theater._meta.db_table), 'theater')


# class MovieTest(TestCase):
#     def test_string(self):
#         mov = Movie(title='movie title')
#         self.assertEqual(str(mov), mov.title)

#     def test_table(self):
#         self.assertEqual(str(Movie._meta.db_table), 'movie')



#tests for form

# class MovieForm_Test(TestCase):
#     def test_typeform_minus_descript(self):
#         form=MovieForm(data={'title': "movie title", 'description': " "})
#         self.assertFalse(form.is_valid())

#     def test_typeform_empty(self):
#         form=MovieForm(data={'url': ""})
#         self.assertFalse(form.is_valid())


class AddTheater_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.ttr=Theater.objects.create(
            name='test add-theater name', 
            user=self.test_user,
            address='7010 rainbow st', 
            comment='optional', 
            url='www.url.com')
        
        self.mov = Movie.objects.create(
            title='mov title', 
            date=self.ttr, 
            url='http://www.test.com',
            description= 'mov desc', 
            review="mov review")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('addtheater'))
        self.assertRedirects(response, '/accounts/login/?next=/movieapp/addtheater/')

    # def test_Logged_in_uses_correct_template(self):
    #     login=self.client.login(username='testuser1', password='P@ssw0rd1')
    #     response=self.client.get(reverse('addmovie'))
    #     self.assertEqual(str(response.context['user']), 'testuser1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'movieapp/addmovie.html')