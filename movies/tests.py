from django.test import TestCase
from datetime import date
from .models import Movie

class MovieModelTest(TestCase):
    def setUp(self):
        Movie.objects.create(
            title='Test Movie',
            release_date=date(2022, 1, 1),
            genre='Action',
            director='Test Director',
            description='This is a test movie.'
        )

    def test_movie_instance(self):
        test_movie = Movie.objects.get(title='Test Movie')
        self.assertEqual(test_movie.title, 'Test Movie')
        self.assertEqual(test_movie.genre, 'Action')
        self.assertEqual(test_movie.director, 'Test Director')
        self.assertEqual(test_movie.description, 'This is a test movie.')
        self.assertEqual(test_movie.release_date, date(2022, 1, 1))

