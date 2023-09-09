import unittest
from unittest import TestCase
from Workshop.custom_list import CustomList


class TestList(TestCase):
    def setUp(self) -> None:
        self.my_list = CustomList()

    def test_check_initialization(self):
        self.my_list = ['Mark']
        self.assertEqual(['Mark'], self.my_list)

    def test_check_append_method_works_correctly(self):

        self.assertEqual(['Mark'], self.my_list.append('Mark'))
        self.assertEqual(['Mark', 'Bisu'], self.my_list.append('Bisu'))

    def test_check_remove_method_pops_element(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.remove(1)
        self.assertEqual('Bisu', result)

        result = self.my_list.remove(0)
        self.assertEqual('Mark', result)

    def test_check_remove_method_raises_index_error(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        with self.assertRaises(IndexError) as ie:
            self.my_list.remove(5)
        self.assertEqual('Index 5 is out of range.', str(ie.exception))

    def test_check_remove_method_returns_message_when_index_is_not_int(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.remove('Hello')
        self.assertEqual(result, 'Please, use an integer.')

    def test_get_method_returns_correctly_the_searching_element(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.get(1)
        self.assertEqual(result, 'Bisu')

        result = self.my_list.get(0)
        self.assertEqual(result, 'Mark')

    def test_get_method_raises_IndexError_when_index_is_out_of_range(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        with self.assertRaises(IndexError) as ie:
            self.my_list.get(7)
        self.assertEqual('Index 7 is out of range.', str(ie.exception))

    def test_get_method_returns_message_when_index_is_not_int(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.get('Hello')
        self.assertEqual(result, 'Please, use an integer.')

    def test_extend_method_returns_list(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.extend(['Hris', 'Yanitsa'])

        self.assertEqual(result, ['Mark', 'Bisu', 'Hris', 'Yanitsa'])

    def test_extend_method_raises_TypeError(self):

        with self.assertRaises(TypeError) as te:
            result = self.my_list.extend(1)
        self.assertEqual('1 is not iterable', str(te.exception))

    def test_insert_method_returns_list(self):
        self.my_list.append('Bisu')
        result = self.my_list.insert(0, 'Mark')

        self.assertEqual(result, ['Mark', 'Bisu'])

    def test_pop_method_pops_and_returns_element_from_the_list(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.pop()

        self.assertEqual(result, 'Bisu')

    def test_pop_method_returns_message_when_the_list_is_empty(self):
        result = self.my_list.pop()

        self.assertEqual(result, 'We can not pop from empty list!')

    def test_method_clear(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.clear()

        self.assertEqual([], self.my_list.list)

    def test_index_method_returns_correct_value(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.index('Bisu')

        self.assertEqual(result, 1)

    def test_index_method_raises_ValueError(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        with self.assertRaises(ValueError) as ve:
            self.my_list.index('Yani')
        self.assertEqual(f'Yani is not in the list!', str(ve.exception))

    def test_count_method_works_correctly(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        self.assertEqual(self.my_list.count('Mark'), 1)

        self.my_list.append('Mark')
        self.assertEqual(self.my_list.count('Mark'), 2)

    def test_len_method_returns_the_length_of_the_list(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        self.assertEqual(self.my_list.__len__(), 2)

    def test_add_first_method_returns_expected_result(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')

        result = self.my_list.add_first('Yani')

        self.assertEqual(result, self.my_list.list)

    def test_dictionize_method_returns_dictionary_with_correct_key_value_pairs(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.append('Yani')

        expected_result = {'Mark': 'Bisu', 'Yani': ' '}

        self.assertEqual(self.my_list.dictionize(), expected_result)

    def test_move_method_works_correctly_and_move_an_element_to_the_end_of_the_list(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.append('Yani')

        result = self.my_list.move('Mark')

        self.assertEqual(result, self.my_list.list)

    def test_move_method_returns_message_when_amount_dose_not_exist(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.append('Yani')

        result = self.my_list.move('Kasia')

        self.assertEqual(result, 'Kasia is not in the list!')

    def test_sum_method_calculates_properly(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.append(3)
        self.my_list.append(['s'])
        self.my_list.append(())

        self.assertEqual(12, self.my_list.sum())

        self.my_list.append('Yanica')

        self.assertEqual(18, self.my_list.sum())

    def test_overbound_returns_the_biggest_value_in_the_list(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.append(3)
        self.my_list.append(['s'])
        self.my_list.append('Yanica')

        self.assertEqual(6, self.my_list.overbound())

    def test_underbound_method_returns_the_smallest_value_in_the_list(self):
        self.my_list.append('Mark')
        self.my_list.append('Bisu')
        self.my_list.append(3)
        self.my_list.append(['s'])
        self.my_list.append('Yanica')
        self.my_list.append(-1)
        self.my_list.append(-20)

        self.assertEqual(-20, self.my_list.underbound())


if '__name__' == '__main__':
    unittest.main()
