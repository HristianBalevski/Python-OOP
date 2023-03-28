from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    FUEL_CONSUMPTION = Vehicle.DEFAULT_FUEL_CONSUMPTION
    FUEL = 80
    CAPACITY = 100
    HORSE_POWER = 120

    def setUp(self) -> None:

        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)
        self.vehicle.capacity = self.CAPACITY
        self.vehicle.horse_power = self.HORSE_POWER

    def test_initialization(self):
        self.setUp()
        self.assertEqual(80, self.FUEL)
        self.assertEqual(100, self.CAPACITY)
        self.assertEqual(120, self.HORSE_POWER)
        self.assertEqual(1.25, self.FUEL_CONSUMPTION)

    def test_drive_raise_error_message_when_we_do_not_have_enough_fuel(self):
        message = "Not enough fuel"

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(70)
        self.assertEqual(message, str(ex.exception))

    def test_drive_works_correctly_when_we_have_enough_fuel(self):
        self.vehicle.drive(50)
        self.assertEqual(17.5, self.vehicle.fuel)

        self.vehicle.drive(14)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_raise_error_when_we_try_to_fill_with_too_much_fuel(self):
        message = "Too much fuel"
        self.setUp()

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual(message, str(ex.exception))

    def test_refuel_add_correctly_fuel(self):
        self.setUp()

        self.vehicle.refuel(10)
        self.assertEqual(90, self.vehicle.fuel)

        self.vehicle.refuel(10)
        self.assertEqual(100, self.vehicle.fuel)

    def test_str_method_returns_correct_message(self):
        message = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(message, self.vehicle.__str__())


if __name__ == '__main__':
    main()
