class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, str) or isinstance(float_value, int):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for index, element in enumerate(value):
            if (index + 1) == len(value) or roman_numerals[element] >= roman_numerals[value[index + 1]]:
                result += roman_numerals[element]
            else:
                result -= roman_numerals[element]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        try:
            number = int(value)
            return cls(number)
        except ValueError:
            return 'wrong type'


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
