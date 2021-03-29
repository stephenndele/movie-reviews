from django.test import TestCase
import datetime as dt
from django.contrib.auth.models import User
from .models import Movie

# Create your tests here.

class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.stephen= User(first_name = 'stephen', last_name ='ndele', password = 'test1234', email ='stephen@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.stephen,User))


    # Testing Save Method
    def test_save_method(self):
        self.stephen.save()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)


class MovieTestClass(TestCase):

    def setUp(self):
        # Creating a new user and saving it
        self.stephen= User(first_name = 'stephen', last_name ='ndele', email ='stephen@gmail.com')
        self.stephen.save_User()

        

        self.new_movie= Movie(title = 'Test Movie',body = 'This is a random test Post',user = self.stephen)
        self.new_movie.save()


    def tearDown(self):
        User.objects.all().delete()
        Movie.objects.all().delete()

   