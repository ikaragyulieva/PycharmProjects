from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.paint = PaintFactory("Paint", 10)

    def test_init(self):
        self.assertEqual("Paint", self.paint.name)
        self.assertEqual(10, self.paint.capacity)
        self.assertEqual({}, self.paint.ingredients)
        self.assertIsInstance(self.paint.name, str)
        self.assertIsInstance(self.paint.capacity, int)
        self.assertIsInstance(self.paint.ingredients, dict)

    def test_add_valid_ingredient_with_enough_space(self):
        self.paint.add_ingredient("yellow", 5)
        self.assertEqual({"yellow": 5}, self.paint.ingredients)

    def test_add_valid_ingredient_without_enough_space_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.paint.add_ingredient("white", 12)

        self.assertEqual("Not enough space in factory", str(ve.exception))
        self.assertEqual({}, self.paint.ingredients)

    def test_add_invalid_ingredient_expect_type_error(self):
        product_type = 'purple'

        with self.assertRaises(TypeError) as ty:
            self.paint.add_ingredient(product_type, 6)

        self.assertEqual(f"Ingredient of type {product_type} not allowed in {self.paint.__class__.__name__}", str(ty.exception))
        self.assertEqual({}, self.paint.ingredients)

    def test_remove_existing_ingredient_with_enough_quantity(self):
        self.paint.ingredients = {'blue': 4, 'red': 6}
        self.paint.remove_ingredient('blue', 2)

        self.assertEqual({'blue': 2, 'red': 6}, self.paint.ingredients)

    def test_remove_existing_ingredient_not_enough_quantity_expect_value_error(self):
        self.paint.ingredients = {'blue': 4, 'red': 6}

        with self.assertRaises(ValueError) as ve:
            self.paint.remove_ingredient('blue', 12)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))
        self.assertEqual({'blue': 4, 'red': 6}, self.paint.ingredients)

    def test_remove_not_existing_ingredient_expect_key_error(self):
        self.paint.ingredients = {'blue': 4, 'red': 6}

        with self.assertRaises(KeyError) as ty:
            self.paint.remove_ingredient('purple', 6)

        self.assertEqual("No such ingredient in the factory", str(ty.exception))
        self.assertEqual({}, self.paint.ingredients)

    def test_property_products(self):
        self.assertEqual(self.paint.ingredients, self.paint.products)


if __name__ == "__main__":
    main()
