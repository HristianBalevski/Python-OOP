import unittest
from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):
    def test_correct_init(self):
        self.toy_store = ToyStore()
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_shelf_not_in_toy_shelf_raise_ex(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("K", "Voltron")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_toy_is_already_in_the_shelf_ex(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("D", "Voltron")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("D", "Voltron")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_raise_ex_place_is_already_taken(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("D", "Voltron")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("D", "Teddy_bear")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_place_toy_successfully(self):
        self.toy_store = ToyStore()
        result = self.toy_store.add_toy("A", "Voltron")

        self.assertEqual(result, "Toy:Voltron placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "Voltron",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_key_that_does_not_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("K", "Voltron")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_in_that_shelf_does_not_exist(self):
        self.toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Voltron")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.toy_store = ToyStore()
        self.toy_store.add_toy("A", "Voltron")
        result = self.toy_store.remove_toy("A", "Voltron")

        self.assertEqual(result, "Remove toy:Voltron successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })


if __name__ == '__main__':
    unittest.main()
