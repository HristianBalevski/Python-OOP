from project import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setup(self):
        self.truck = TruckDriver('John', 10, )

    def test_correct_initialization(self):
        self.setup()
        self.assertEqual('John', self.truck.name)
        self.assertEqual(10, self.truck.money_per_mile)
        self.assertEqual({}, self.truck.available_cargos)
        self.assertEqual(0, self.truck.earned_money)
        self.assertEqual(0, self.truck.miles)

    def test_earned_money_raise_error_when_value_is_negative_number(self):
        with self.assertRaises(ValueError) as ex:
            self.setup()
            self.truck.earned_money = -1
        self.assertEqual(f"{self.truck.name} went bankrupt.", str(ex.exception))

    def test_bankrupt(self):
        self.setup()
        self.truck.money_per_mile = 0.01
        self.truck.add_cargo_offer('Sofia', 2000)

        with self.assertRaises(ValueError) as ex:
            self.truck.drive_best_cargo_offer()
        self.assertEqual(f"{self.truck.name} went bankrupt.", str(ex.exception))

    def test_add_cargo_raise_error_when_the_offer_is_in_dictionary(self):
        self.setup()
        self.truck.add_cargo_offer('Sofia', 120)

        with self.assertRaises(Exception) as ex:
            self.truck.add_cargo_offer('Sofia', 120)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_add_offer_when_the_offer_is_not_in_dictionary(self):
        self.setup()
        result = self.truck.add_cargo_offer('Sofia', 120)

        self.assertEqual({'Sofia': 120}, self.truck.available_cargos)
        self.assertEqual(result, f"Cargo for 120 to Sofia was added as an offer.")

    def test_best_cargo_offer_raise_error_when_no_offers_available(self):
        self.setup()
        result = self.truck.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_best_cargo_offer_with_available_offer(self):
        self.setup()
        self.truck.add_cargo_offer('Sofia', 100)
        self.truck.add_cargo_offer('Varna', 200)

        result = self.truck.drive_best_cargo_offer()

        self.assertEqual(result, f'{self.truck.name} is driving 200 to Varna.')
        self.assertEqual(2000, self.truck.earned_money)
        self.assertEqual(200, self.truck.miles)

    def test_check_activities(self):
        self.setup()
        self.truck.earned_money = 20000
        self.truck.check_for_activities(10000)
        self.assertEqual(self.truck.earned_money, 8250)

    def test_eat(self):
        self.setup()
        self.truck.earned_money = 100
        self.truck.eat(250)
        self.truck.eat(500)
        self.assertEqual(60, self.truck.earned_money)

    def test_sleep(self):
        self.setup()
        self.truck.earned_money = 100
        self.truck.sleep(1000)
        self.truck.sleep(3000)
        self.assertEqual(10, self.truck.earned_money)

    def test_pump_gas(self):
        self.setup()
        self.truck.earned_money = 1000
        self.truck.pump_gas(1500)
        self.truck.pump_gas(4500)
        self.assertEqual(0, self.truck.earned_money)

    def test_repair_truck(self):
        self.setup()
        self.truck.earned_money = 16000
        self.truck.repair_truck(10000)
        self.truck.repair_truck(50000)
        self.assertEqual(1000, self.truck.earned_money)

    def test_repr(self):
        self.setup()
        self.assertEqual(str(self.truck), f"John has 0 miles behind his back.")


if __name__ == '__main__':
    unittest.main()

