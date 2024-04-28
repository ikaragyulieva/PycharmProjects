from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self) -> None:
        self.robot = ClimbingRobot("Mountain", "testing", 5, 50)

    def test_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("testing", self.robot.part_type)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(50, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

        self.assertIsInstance(self.robot.category, str)
        self.assertIsInstance(self.robot.part_type, str)
        self.assertIsInstance(self.robot.memory, int)
        self.assertIsInstance(self.robot.capacity, int)
        self.assertIsInstance(self.robot.installed_software, list)

    def test_category_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot_test = ClimbingRobot("City", "testing", 5, 10)

        self.assertEqual("Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ve.exception))

    def test_get_used_capacity(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 5, 'memory_consumption': 50}
        software_2 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 50}
        self.robot.installed_software = [software_2, software_1]
        result = self.robot.get_used_capacity()

        self.assertEqual(15, result)

    def test_get_available_capacity(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 2, 'memory_consumption': 50}
        software_2 = {'name': 'Test1', 'capacity_consumption': 1, 'memory_consumption': 50}
        self.robot.installed_software = [software_2, software_1]
        result = self.robot.get_available_capacity()

        self.assertEqual(2, result)

        software_1 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 50}
        software_2 = {'name': 'Test1', 'capacity_consumption': 1, 'memory_consumption': 50}
        self.robot.installed_software = [software_2, software_1]
        result = self.robot.get_available_capacity()

        self.assertEqual(-6, result)

    def test_used_memory(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 10}
        software_2 = {'name': 'Test1', 'capacity_consumption': 1, 'memory_consumption': 20}
        self.robot.installed_software = [software_2, software_1]
        result = self.robot.get_used_memory()

        self.assertEqual(30, result)

    def test_get_available_memory(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 10}
        software_2 = {'name': 'Test1', 'capacity_consumption': 1, 'memory_consumption': 20}
        self.robot.installed_software = [software_2, software_1]
        result = self.robot.get_available_memory()

        self.assertEqual(20, result)

        software_1 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 50}
        software_2 = {'name': 'Test1', 'capacity_consumption': 1, 'memory_consumption': 20}
        self.robot.installed_software = [software_2, software_1]
        result = self.robot.get_available_memory()

        self.assertEqual(-20, result)

    def test_installed_software_successfully(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 4, 'memory_consumption': 20}
        result = self.robot.install_software(software_1)

        self.assertEqual("Software 'Test1' successfully installed on Mountain part.", result)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(50, self.robot.memory)
        self.assertEqual([{'capacity_consumption': 4, 'memory_consumption': 20, 'name': 'Test1'}],
                         self.robot.installed_software)

    def test_unsuccessful_installation_not_enough_capacity(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 20}
        result = self.robot.install_software(software_1)

        self.assertEqual("Software 'Test1' cannot be installed on Mountain part.", result)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(50, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_unsuccessful_installation_not_enough_memory(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 2, 'memory_consumption': 100}
        result = self.robot.install_software(software_1)

        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(50, self.robot.memory)
        self.assertEqual("Software 'Test1' cannot be installed on Mountain part.", result)

    def test_unsuccessful_installation_not_enough_capacity_and_memory(self):
        software_1 = {'name': 'Test1', 'capacity_consumption': 10, 'memory_consumption': 100}
        result = self.robot.install_software(software_1)

        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(5, self.robot.capacity)
        self.assertEqual(50, self.robot.memory)
        self.assertEqual("Software 'Test1' cannot be installed on Mountain part.", result)


if __name__ == "__main__":
    main()
