from unittest import TestCase, main
from Worker.worker import Worker


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("TestGuy", 25000, 100)

    def test_initialization(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_energy_expecting_money_increase_and_energy_decrease(self):
        expected_energy = self.worker.energy - 2
        expected_money = self.worker.salary * 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_when_worker_has_no_energy_expecting_raise_error_message(self):
        self.worker.energy = 0  # arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))  # assert

    def test_increment_energy_with_one_when_resting(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_valid_string(self):
        self.assertEqual(
            f'{self.worker.name} has saved {self.worker.money} money.',
            self.worker.get_info()
        )

if __name__ == '__main__':
    main()
