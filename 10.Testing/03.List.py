class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):

    def test_add_integer_to_the_list(self):
        data = IntegerList()

        self.assertEqual([], data._IntegerList__data)

    def test_pass_wrong_elements(self):
        data = IntegerList('fdsfs', 3.4)
        self.assertEqual([], data._IntegerList__data)

    def test_add_only_integers_to_the_list(self):
        data = IntegerList('fdsfs', 5)
        self.assertEqual([5], data._IntegerList__data)

    def test_get_data(self):
        data = IntegerList('fdsfs', 5)
        self.assertEqual([5], data._IntegerList__data)

        result = data.get_data()
        self.assertEqual([5], result)

    def test_raise_error_when_try_to_add_wrong_data(self):
        data = IntegerList(5)
        self.assertEqual([5], data._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            data.add('3')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_works_correctly_when_add_correct_element(self):
        data = IntegerList(5)

        data.add(10)
        self.assertEqual([5, 10], data._IntegerList__data)

    def test_remove_element_from_index(self):
        data = IntegerList(5)

        data.remove_index(0)
        self.assertEqual([], data._IntegerList__data)

    def test_raise_error_when_try_to_remove_invalid_index(self):
        data = IntegerList(5)

        with self.assertRaises(IndexError) as ex:

            data.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_and_return_an_element_from_specific_index(self):
        data = IntegerList(5)

        result = data.remove_index(0)
        self.assertEqual(5, result)

    def test_get_with_index_greater_or_equal_to_the_length_of_the_list(self):
        data = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            data.get(2)
        self.assertEqual('Index is out of range', str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            data.get(1)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_return_valid_index(self):
        data = IntegerList(5)

        result = data.get(0)
        self.assertEqual(5, result)

    def test_raise_error_when_insert_greater_or_equal_index(self):
        data = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            data.insert(2, 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_raise_error_when_try_to_insert_incorrect_data_type(self):
        data = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            data.insert(0, '1')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_element_on_correct_index(self):
        data = IntegerList(5)

        data.insert(0, 1)
        self.assertEqual([1, 5], data._IntegerList__data)

    def test_get_biggest_return_the_biggest_integer(self):
        data = IntegerList(5, 10, 100, -500, 0, -345)
        result = data.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        data = IntegerList(5, 10, 100, -500, 0, -345)
        result = data.get_index(10)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()