from unittest import TestCase, main

# from CarManager.car_manager import Car


class TestCarManager(TestCase):

    def setUp(self) -> None:
        self.car = Car("BMW", "M3", 10, 100)

    def test_correct_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M3", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "M3", 10, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "", 10, 100)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_0_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "M3", 0, 100)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_0_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "M3", 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_zero_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_fuel_than_capacity_fills_to_capacity(self):
        self.car.refuel(110)

        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(2)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_valid_fuel(self):
        self.car.refuel(100)
        self.car.drive(10)

        self.assertEqual(99, self.car.fuel_amount )


if __name__ == "__main__":
    main()
