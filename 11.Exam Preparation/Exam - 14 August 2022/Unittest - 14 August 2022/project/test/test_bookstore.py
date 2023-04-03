from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_initialization(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_setter_raise_error_when_value_is_equal_or_bellow_zero(self):
        message = f"Books limit of 0 is not valid"

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual(message, str(ve.exception))

    def test_len_returns_proper_counter(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }
        result = self.bookstore.__len__()
        self.assertEqual(9, result)

    def test_receive_book_raise_error_when_limit_is_reached(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            'Animal Farm': 2
        }

        message = "Books limit is reached. Cannot receive more books!"

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Automatic Habits', 3)
        self.assertEqual(message, str(ex.exception))

    def test_receive_book_when_there_is_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }

        result = self.bookstore.receive_book('Automatic Habits', 1)

        expected_library = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3,
            'Automatic Habits': 1
        }

        expected_result = "1 copies of Automatic Habits are available in the bookstore."

        self.assertEqual(expected_library, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(len(self.bookstore), 10)
        self.assertEqual(expected_result, result)

    def test_receive_book_when_book_is_in_library_and_we_get_new_quantities(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            'Animal Farm': 2
        }

        result = self.bookstore.receive_book('Animal Farm', 2)

        expected_library = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            'Animal Farm': 4
        }
        message = "4 copies of Animal Farm are available in the bookstore."

        self.assertEqual(message, result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_library)
        self.assertEqual(len(self.bookstore), 10)

    def test_sell_book_raise_error_when_book_is_not_available(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }

        message = "Book Automatic Habits doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Automatic Habits', 1)
        self.assertEqual(message, str(ex.exception))

    def test_sell_book_len_self_is_less_when_we_sell_last_book(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }

        self.bookstore.sell_book('1984', 3)
        del self.bookstore.availability_in_store_by_book_titles['1984']
        expected_library = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3}
        self.assertEqual(len(self.bookstore), 6)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_library)
        self.assertEqual(self.bookstore.total_sold_books, 3)

    def test_sell_book_raise_error_when_there_is_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }

        message = "To Kill a Mockingbird has not enough copies to sell. Left: 3"

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('To Kill a Mockingbird', 4)
        self.assertEqual(message, str(ex.exception))
        self.assertEqual(len(self.bookstore), 9)

    def test_sell_book_works_correctly_when_we_sell_book_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }

        self.assertEqual(len(self.bookstore), 9)
        result = self.bookstore.sell_book('Rich Dad Poor Dad', 2)
        expected_library = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 1,
            '1984': 3
        }

        message = "Sold 2 copies of Rich Dad Poor Dad"

        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_library)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual(message, result)
        self.assertEqual(len(self.bookstore), 7)

        self.bookstore.sell_book('1984', 1)
        self.assertEqual(3, self.bookstore.total_sold_books)
        self.assertEqual(len(self.bookstore), 6)

    def test_str(self):
        self.bookstore.availability_in_store_by_book_titles = {
            'To Kill a Mockingbird': 3,
            'Rich Dad Poor Dad': 3,
            '1984': 3
        }

        self.bookstore.sell_book('Rich Dad Poor Dad', 2)

        expected_result = "Total sold books: 2\n"\
                          "Current availability: 7\n" \
                          " - To Kill a Mockingbird: 3 copies\n" \
                          " - Rich Dad Poor Dad: 1 copies\n" \
                          " - 1984: 3 copies"

        self.assertEqual(expected_result, self.bookstore.__str__())


if __name__ == '__main__':
    main()