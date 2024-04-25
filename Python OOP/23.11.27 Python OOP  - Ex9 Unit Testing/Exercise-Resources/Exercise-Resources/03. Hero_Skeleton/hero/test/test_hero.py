from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("test", 10, 85.6, 10.6)
        self.enemy_hero = Hero("test2", 12, 60.7, 32.1)

    def test_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(85.6, self.hero.health)
        self.assertEqual(10.6, self.hero.damage)

    def test_battle_with_myself_except_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_option_low_hero_health_expected_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_option_low_enemy_hero_health_expected_value_error(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_battle_when_both_heroes_with_health_below_0_after_fight_expect_string(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 100

        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))

    def test_battle_when_hero_wins_expect_increase_in_level_health_damage(self):
        self.hero.damage = 100
        self.enemy_hero.damage = 5
        expected_health = 30.599999999999
        expected_level = 11
        expected_damage = 105
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        # self.assertEqual()
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual(expected_level, self.hero.level)
        self.assertAlmostEqual(expected_health, self.hero.health)

    def test_battle_when_hero_loses_expect_increase_level_health_damage_enemy_hero(self):
        self.hero.damage = 5
        self.enemy_hero.damage = 100
        expected_health = 15.7
        expected_level = 13
        expected_damage = 105
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_damage, self.enemy_hero.damage)
        self.assertEqual(expected_level, self.enemy_hero.level)
        self.assertAlmostEqual(expected_health, self.enemy_hero.health)

    def test_string(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\n"
                         f"Health: {self.hero.health}\n"
                         f"Damage: {self.hero.damage}\n", self.hero.__str__())


if __name__ == "__main__":
    main()
