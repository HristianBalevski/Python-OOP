from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    DEFAULT_NAME = 'Lancelot'
    DEFAULT_LEVEL = 10
    DEFAULT_HEALTH = 100
    DEFAULT_DAMAGE = 10

    def setUp(self) -> None:
        self.hero = Hero(self.DEFAULT_NAME, self.DEFAULT_LEVEL, self.DEFAULT_HEALTH, self.DEFAULT_DAMAGE)

    def test_initialization(self):
        self.assertEqual(self.hero.username, self.DEFAULT_NAME)
        self.assertEqual(self.hero.level, self.DEFAULT_LEVEL)
        self.assertEqual(self.hero.health, self.DEFAULT_HEALTH)
        self.assertEqual(self.hero.damage, self.DEFAULT_DAMAGE)

    def test_battle_raise_error_when_enemy_name_equal_to_username(self):
        enemy = Hero(self.DEFAULT_NAME, 8, 100, 5)
        message = "You cannot fight yourself"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertTrue(message, str(ex.exception))

    def test_battle_raise_error_when_hero_is_dead(self):
        enemy = Hero('Mutare Drake', 8, 100, 5)
        message = "Your health is lower than or equal to 0. You need to rest"
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual(message, str(ve.exception))

    def test_battle_raise_error_when_enemy_is_dead(self):
        enemy = Hero('Mutare Drake', 8, 0, 5)
        message = f"You cannot fight {enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual(message, str(ve.exception))

    def test_battle_both_heroes_die(self):
        attacker = Hero('Kilgor', 10, 100, 75)
        enemy = Hero('Mutare Drake', 10, 100, 75)

        result = self.hero.battle(enemy)
        attacker.health = enemy.health - (enemy.level * enemy.damage)
        enemy.health = enemy.health - (enemy.level * enemy.damage)

        self.assertEqual('Draw', result)
        self.assertEqual(enemy.health, attacker.health)

    def test_battle_attacker_win(self):
        enemy_level, enemy_health, enemy_damage = 1, 100, 8
        enemy = Hero('Mutare Drake', enemy_level, enemy_health, enemy_damage)

        result = self.hero.battle(enemy)
        enemy_health_after_the_battle = enemy_health - (self.DEFAULT_LEVEL * self.DEFAULT_DAMAGE)
        attacker_health_after_the_battle = self.DEFAULT_HEALTH - (enemy_level * enemy_damage)

        self.assertEqual('You win', result)
        self.assertEqual(enemy_health_after_the_battle, enemy.health)
        self.assertEqual(self.hero.level, self.DEFAULT_LEVEL + 1)
        self.assertEqual(self.hero.health, attacker_health_after_the_battle + 5)

    def test_enemy_win(self):
        attacker_level, attacker_health, attacker_damage = 1, 100, 8
        attacker = Hero('Kilgor', attacker_level, attacker_health, attacker_damage)
        enemy = Hero('Mutare Drake', self.DEFAULT_LEVEL, self.DEFAULT_HEALTH, self.DEFAULT_DAMAGE)

        result = attacker.battle(enemy)
        attacker_health_after_the_battle = attacker_health - (self.DEFAULT_LEVEL * self.DEFAULT_DAMAGE)
        enemy_health_after_the_battle = self.DEFAULT_HEALTH - (attacker_level * attacker_damage)

        self.assertEqual('You lose', result)
        self.assertEqual(attacker_health_after_the_battle, attacker.health)
        self.assertEqual(enemy_health_after_the_battle + 5, enemy.health)
        self.assertEqual(enemy.level, self.DEFAULT_LEVEL + 1)
        self.assertEqual(enemy.damage, self.DEFAULT_DAMAGE + 5)

    def test_str_returns_correct_string(self):
        message = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(message, str(self.hero))


if __name__ == '__main__':
    main()
