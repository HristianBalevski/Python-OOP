from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Die Hard', 1988, 8)

    def test_initialization(self):
        self.movie.name = 'Die Hard'
        self.movie.year = 1988
        self.movie.rating = 8
        self.movie.actors = []

    def test_setter_raise_error_when_name_is_empty_string(self):

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_setter_raise_error_when_year_is_less_than_minimum(self):

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_when_actor_not_in_actors(self):
        self.movie.add_actor('Bruce Willis')
        result = ['Bruce Willis']
        self.assertEqual(self.movie.actors, result)
        self.assertEqual(1, len(self.movie.actors))

        self.movie.add_actor('Alan Rickman')
        result2 = ['Bruce Willis', 'Alan Rickman']
        self.assertEqual(self.movie.actors, result2)
        self.assertEqual(2, len(self.movie.actors))

    def test_add_actor_returns_message_when_actor_exist_in_actors(self):
        self.movie.add_actor('Bruce Willis')
        message = "Bruce Willis is already added in the list of actors!"

        result = self.movie.add_actor('Bruce Willis')
        self.assertEqual(message, result)
        self.assertEqual(1, len(self.movie.actors))

    def test__gt__when_rating_is_greater_than_other(self):
        first_movie = Movie('Troy', 2004, 8.2)
        second_movie = Movie('Rambo First Blood', 1982, 7)

        result = str(first_movie > second_movie)
        self.assertEqual('"Troy" is better than "Rambo First Blood"', result)

        third_movie = Movie('The Lord of the Rings', 2001, 9)
        second_result = str(first_movie > third_movie)
        self.assertEqual(second_result, '"The Lord of the Rings" is better than "Troy"')

    def test__repr__(self):
        self.movie.add_actor('Bruce Willis')
        self.movie.add_actor('Alan Rickman')
        self.movie.add_actor('Bonnie Bedelia')

        result = f"Name: Die Hard\n" \
                 f"Year of Release: 1988\n" \
                 f"Rating: 8.00\n" \
                 f"Cast: Bruce Willis, Alan Rickman, Bonnie Bedelia"

        self.assertEqual(result, self.movie.__repr__())


if __name__ == '__main__':
    main()
