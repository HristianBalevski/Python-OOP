class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class TestCarManager(unittest.TestCase):
    def setup(self):
        self.car = Car('Audi', 'A3', 7, 100)

    def test_correct_initialization(self):
        self.setup()
        self.assertEqual('Audi', self.car.make)
        self.assertEqual('A3', self.car.model)
        self.assertEqual(7, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_raise_error_when_value_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_raise_error_when_value_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raise_error_when_fuel_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raise_error_when_fuel_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_amount_raise_error_when_amount_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raise_error_when_fuel_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_correct_fuel(self):
        self.setup()
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_with_fuel_over_the_capacity(self):
        self.setup()
        self.car.refuel(120)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_raise_error_when_we_do_not_have_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.setup()
            self.car.refuel(10)
            self.car.drive(500)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_decrease_properly_amount_of_the_fuel(self):
        self.setup()
        self.car.refuel(10)
        self.car.drive(50)
        self.assertEqual(6.5, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()