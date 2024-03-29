class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def test_size_increase_after_eating(self):
        cat = Cat('Honey')

        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        cat = Cat('Honey')

        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)

    def test_cannot_eat_after_eating(self):
        cat = Cat('Honey')

        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cannot_sleep_when_is_not_fed(self):
        cat = Cat('Honey')
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            self.assertTrue(cat.sleep())
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat('Honey')
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
