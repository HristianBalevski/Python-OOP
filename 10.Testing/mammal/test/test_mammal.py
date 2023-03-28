from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    DEFAULT_NAME = 'John'
    DEFAULT_TYPE = 'Human'
    DEFAULT_SOUND = 'Speaking'

    def setUp(self) -> None:
        self.mammal = Mammal(self.DEFAULT_NAME, self.DEFAULT_TYPE, self.DEFAULT_SOUND)

    def test_initialization_works_correctly(self):
        self.setUp()
        self.assertEqual('John', self.DEFAULT_NAME)
        self.assertEqual('Human', self.DEFAULT_TYPE)
        self.assertEqual('Speaking', self.DEFAULT_SOUND)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_message(self):
        message = self.mammal.make_sound()
        self.assertEqual(message, f"{self.DEFAULT_NAME} makes {self.DEFAULT_SOUND}")

    def test_get_kingdom_returns_proper_string(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_returns_proper_message(self):
        message = self.mammal.info()
        self.assertEqual(message, f"{self.DEFAULT_NAME} is of type {self.DEFAULT_TYPE}")


if __name__ == '__main__':
    main()