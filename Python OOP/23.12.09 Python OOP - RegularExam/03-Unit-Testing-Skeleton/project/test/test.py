from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("Madrid")

    def test_init(self):
        self.assertEqual("Madrid", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)
        self.assertIsInstance(self.station.name, str)

    def test_invalid_name_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_station = RailwayStation("")

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_station = RailwayStation("3")

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival(self):
        self.station.new_arrival_on_board("test_train")

        self.assertEqual(deque(['test_train']), self.station.arrival_trains)

    def test_train_arrival_waiting(self):
        self.station.arrival_trains = deque(['test1', 'test_train'])
        result = self.station.train_has_arrived('test_train')
        self.assertEqual("There are other trains to arrive before test_train.", result)
        self.assertEqual(deque([]), self.station.departure_trains)
        self.assertEqual(deque(['test1', 'test_train']), self.station.arrival_trains)

    def test_train_arrival(self):
        self.station.arrival_trains = deque(['test_train', 'test1'])
        result = self.station.train_has_arrived('test_train')
        self.assertEqual("test_train is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(['test_train']), self.station.departure_trains)
        self.assertEqual(deque(['test1']), self.station.arrival_trains)

    def test_train_has_left_true(self):

        self.station.departure_trains = deque(['test_train', 'test1'])
        result = self.station.train_has_left('test_train')
        self.assertTrue(result)
        self.assertEqual(deque(['test1']), self.station.departure_trains)
        self.assertEqual(deque([]), self.station.arrival_trains)

    def test_train_has_left_false(self):

        self.station.departure_trains = deque(['test1', 'test_train'])
        result = self.station.train_has_left('test_train')
        self.assertFalse(result)
        self.assertEqual(deque(['test1', 'test_train']), self.station.departure_trains)
        self.assertEqual(deque([]), self.station.arrival_trains)


if __name__ == "__main__":
    main()
