class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):

    def test_check_if_the_worker_is_initialized_with_the_correct_name_salary_and_energy(self):
        worker = Worker('Hris', 100, 10)

        self.assertEqual('Hris', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_check_if_energy_is_incremented_after_the_rest(self):
        worker = Worker('Hris', 100, 10)

        self.assertEqual(10, worker.energy)

        worker.rest()

        self.assertEqual(11, worker.energy)

        worker.rest()

        self.assertEqual(12, worker.energy)

    def test_if_exception_is_raise_when_energy_is_zero_or_negative_number(self):
        worker = Worker('Hris', 100, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_the_money_increase_after_work(self):
        worker = Worker('Hris', 100, 10)

        self.assertEqual(0, worker.money)

        worker.work()

        self.assertEqual(100, worker.money)

        worker.work()

        self.assertEqual(200, worker.money)

    def test_if_the_energy_is_decreased_after_work(self):
        worker = Worker('Hris', 100, 10)

        self.assertEqual(10, worker.energy)

        worker.work()

        self.assertEqual(9, worker.energy)

    def test_get_info(self):
        worker = Worker('Hris', 100, 10)

        result = worker.get_info()
        expected = 'Hris has saved 0 money.'

        worker.get_info()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
