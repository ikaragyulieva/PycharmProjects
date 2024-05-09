from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plant = Plantation(10)

    def test_init(self):
        self.assertEqual(10, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

        self.assertIsInstance(self.plant.size, int)
        self.assertIsInstance(self.plant.plants, dict)
        self.assertIsInstance(self.plant.workers, list)

    def test_invalid_size_expect_value_error(self):
        plant_test = Plantation(0)

        self.assertEqual(0, plant_test.size)

        with self.assertRaises(ValueError) as ve:
            plant_test = Plantation(-10)

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_new_worker(self):
        result = self.plant.hire_worker("Fontanero")

        self.assertEqual("Fontanero successfully hired.", result)
        self.assertEqual(["Fontanero"], self.plant.workers)
        self.assertEqual({}, self.plant.plants)

    def test_already_existing_worker(self):
        self.plant.workers = ["Fontanero", "Plantero"]

        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker("Plantero")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Fontanero", "Plantero"], self.plant.workers)
        self.assertEqual({}, self.plant.plants)

    def test_dunder_len(self):
        self.plant.workers = ["Fontanero", "Plantero"]
        self.plant.plants = {"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}

        result = self.plant.__len__()
        self.assertEqual(3, result)

    def test_planting_with_no_existing_worker_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Plantero", "flowers")

        self.assertEqual("Worker with name Plantero is not hired!", str(ve.exception))
        self.assertEqual([], self.plant.workers)
        self.assertEqual({}, self.plant.plants)

    def test_planting_not_capacity_expect_value_error(self):
        self.plant.size = 3
        self.plant.workers = ["Fontanero", "Plantero"]
        self.plant.plants = {"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}

        with self.assertRaises(ValueError) as ve:
            self.plant.planting("Plantero", "flowers")

        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertEqual(["Fontanero", "Plantero"], self.plant.workers)
        self.assertEqual({"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}, self.plant.plants)

    def test_successful_planting_with_worker_already_in_plants(self):
        self.plant.workers = ["Fontanero", "Plantero"]
        self.plant.plants = {"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}

        result = self.plant.planting("Plantero", "tree")

        self.assertEqual("Plantero planted tree.", result)
        self.assertEqual(["Fontanero", "Plantero"], self.plant.workers)
        self.assertEqual({"Plantero": ["flowers", "flower2", "tree"], "Fontanero": ["trees"]}, self.plant.plants)

    def test_successful_planting_with_worker_not_in_plants(self):
        self.plant.workers = ["Fontanero", "Plantero", "Test"]
        self.plant.plants = {"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}

        result = self.plant.planting("Test", "tree")

        self.assertEqual("Test planted it's first tree.", result)
        self.assertEqual(["Fontanero", "Plantero", "Test"], self.plant.workers)
        self.assertEqual({"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"], "Test": ["tree"]}, self.plant.plants)

    def test_str_dunder_method(self):
        self.plant.workers = ["Fontanero", "Plantero"]
        self.plant.plants = {"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}
        result = self.plant.__str__()

        self.assertEqual("Plantation size: 10\n"
                         "Fontanero, Plantero\n"
                         "Plantero planted: flowers, flower2\n"
                         "Fontanero planted: trees",
                         result)

    def test_repr_dunder_method(self):
        self.plant.workers = ["Fontanero", "Plantero"]
        self.plant.plants = {"Plantero": ["flowers", "flower2"], "Fontanero": ["trees"]}
        result = self.plant.__repr__()

        self.assertEqual("Size: 10\nWorkers: Fontanero, Plantero", result)


if __name__ == "__main__":
    main()
