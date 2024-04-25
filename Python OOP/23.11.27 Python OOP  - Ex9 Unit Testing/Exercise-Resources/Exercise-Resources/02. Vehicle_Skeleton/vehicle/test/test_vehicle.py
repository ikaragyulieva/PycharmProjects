from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(52.5, 10.6)

    def test_init(self):
        self.assertEqual(52.5, self.vehicle.fuel)
        self.assertEqual(52.5, self.vehicle.capacity)
        self.assertEqual(10.6, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attribute_types(self):
        # self.assertIsInstance(self.vehicle.fuel, float)
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_drive_with_not_enough_fuel_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_expect_fuel_decrease(self):
        expected_result = 33.75
        self.vehicle.drive(15)

        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_fuel_expect_fuel_increase(self):
        self.vehicle.drive(15)
        self.vehicle.refuel(10.5)

        self.assertEqual(44.25, self.vehicle.fuel)

    def test_string_method(self):
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} "
                         f"horse power with {self.vehicle.fuel} fuel left "
                         f"and {self.vehicle.fuel_consumption} fuel consumption",
                         self.vehicle.__str__()
                         )


if __name__ == "__main__":
    main()
