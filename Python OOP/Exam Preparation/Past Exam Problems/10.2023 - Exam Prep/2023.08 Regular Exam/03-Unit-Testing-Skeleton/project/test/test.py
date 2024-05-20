from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("BMW", "M3", 10000, 25000.0)

    def test_init(self):
        self.assertEqual("BMW", self.car.model)
        self.assertEqual("M3", self.car.car_type)
        self.assertEqual(10000, self.car.mileage)
        self.assertEqual(25000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

        self.assertIsInstance(self.car.model, str)
        self.assertIsInstance(self.car.car_type, str)
        self.assertIsInstance(self.car.mileage, int)
        self.assertIsInstance(self.car.price, float)
        self.assertIsInstance(self.car.repairs, list)

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar("BMW", "M3", 10000, 0.99)

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar("BMW", "M3", 10000, -20000)

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar("BMW", "M3", 10000, 1.00)

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_invalid_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar("BMW", "M3", 10, 25000.0)

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar("BMW", "M3", 100, 25000.0)

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_car = SecondHandCar("BMW", "M3", -10000, 25000.0)

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_higher_promotional_price_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(30000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(-30000)

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_set_promotional_price(self):
        result = self.car.set_promotional_price(20000.0)

        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(20000.0, self.car.price)

    def test_need_repair_not_enough_money_expect_string(self):
        result = self.car.need_repair(20500.50, "Test Repair")
        self.assertEqual('Repair is impossible!', result)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_enough_money_expect_string(self):
        result = self.car.need_repair(1000, "Test Repair")

        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(26000, self.car.price)
        self.assertEqual(["Test Repair"], self.car.repairs)

    def test_gt_not_matching_models_expect_string_message(self):
        test_car = SecondHandCar("BMW", "M1", 10000, 25000.0)
        result = self.car.__gt__(test_car)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_matching_models(self):
        test_car = SecondHandCar("BMW", "M3", 10000, 20000.0)
        result = self.car.__gt__(test_car)
        self.assertEqual(True, result)

    def test_str_method(self):
        result = self.car.__str__()

        self.assertEqual("Model BMW | Type M3 | Milage 10000km\nCurrent price: 25000.00 | Number of Repairs: 0", result)

if __name__ == "__main__":
    main()
