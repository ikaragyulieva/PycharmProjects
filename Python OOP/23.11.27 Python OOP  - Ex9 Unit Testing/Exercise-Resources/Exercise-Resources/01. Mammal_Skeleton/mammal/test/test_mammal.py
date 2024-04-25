from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    
    def setUp(self):
        self.mammal = Mammal("Tom", "cat", "miau")

    def test_init(self):
        self.assertEqual("Tom", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("miau", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_expecting_string_with_the_sound_and_animal_name(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom_expect_animal_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_expect_string(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == "__main__":
    main()