from sys import maxsize


class CustomList:
    def __init__(self, *args):
        self.list = [*args]

    def append(self, value):
        self.list.append(value)

        return self.list

    def remove(self, index):
        if isinstance(index, int):
            try:
                result = self.list.pop(index)
                return result
            except IndexError:
                raise IndexError(f'Index {index} is out of range.')
        else:
            return 'Please, use an integer.'

    def get(self, index):
        if isinstance(index, int):
            try:
                return self.list[index]
            except IndexError:
                raise IndexError(f'Index {index} is out of range.')
        else:
            return 'Please, use an integer.'

    def extend(self, iterable):
        try:
            self.list.extend(iterable)
            return self.list

        except TypeError:
            raise TypeError(f'{iterable} is not iterable')

    def insert(self, index, value):
        # Here we do not need to check for the valid index because if we specify an index greater than list length we do
        # not get any exception. Instead, the value is inserted at the end of the list.
        self.list.insert(index, value)
        return self.list

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop()

        return 'We can not pop from empty list!'

    def clear(self):
        self.list.clear()

    def index(self, value):
        try:
            return self.list.index(value)
        except ValueError:
            raise ValueError(f'{value} is not in the list!')

    def count(self, value):
        return self.list.count(value)

    def reverse(self):
        # Here we can also use self.list[::-1] if we do not want to reverse the list forever.
        return list(reversed(self.list))

    def copy(self):
        copy_of_the_list = self.list.copy()
        return copy_of_the_list

    def __len__(self):
        return len(self.list)

    def add_first(self, value):
        # We have many options to do this operation.
        # Here are some examples:
        # self.list.insert(0, value)
        # [value] + self.list
        # second_list = [value] second_list.extend(self.list)
        self.list = [value, *self.list]
        return self.list

    def dictionize(self):
        my_dict = {}

        for position in range(len(self.list)):
            if position % 2 == 0:
                if position + 1 >= len(self.list):
                    my_dict[self.list[position]] = ' '
                else:
                    my_dict[self.list[position]] = self.list[position + 1]

        return my_dict

    def move(self, amount):
        if amount in self.list:
            index = self.list.index(amount)
            element = self.list.pop(index)
            self.list.append(element)

            return self.list

        return f'{amount} is not in the list!'

    def sum(self):
        result = 0

        for element in self.list:
            if isinstance(element, int) or isinstance(element, float):
                result += element
            else:
                result += len(element)

        return result

    def overbound(self):
        biggest_value = -maxsize

        for element in self.list:
            if isinstance(element, int) or isinstance(element, float):
                if element > biggest_value:
                    biggest_value = element
            else:
                length = len(element)
                if length > biggest_value:
                    biggest_value = length

        return biggest_value

    def underbound(self):
        smallest_value = maxsize

        for element in self.list:
            if isinstance(element, int) or isinstance(element, float):
                if element < smallest_value:
                    smallest_value = element
            else:
                length = len(element)
                if length < smallest_value:
                    smallest_value = length

        return smallest_value



