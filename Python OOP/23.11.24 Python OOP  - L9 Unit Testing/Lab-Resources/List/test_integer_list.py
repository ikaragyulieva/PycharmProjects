from unittest import TestCase, main

from List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(
            '50',
            1,
            False,
            3.5,
            2,
            3
        )

    def test_correct_init_and_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_operation_adds_integer_to_the_list(self):
        expected_data = self.integer_list.get_data() + [5]
        self.integer_list.add(5)
        self.assertEqual(expected_data, self.integer_list.get_data())

    def test_add_operation_with_float_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(3.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_operation_with_out_of_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index_removes_element(self):
        expected_result = [1, 3]
        deleted_element = 2
        actual_deleted_element = self.integer_list.remove_index(1)

        self.assertEqual(expected_result, self.integer_list.get_data())
        self.assertEqual(deleted_element, actual_deleted_element)

    def test_get_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_operation_with_valid_index_returns_element(self):
        expected_element = 2
        actual_element = self.integer_list.get(1)

        self.assertEqual(expected_element, actual_element)

    def test_insert_operation_integer_on_valid_index_expected_insert_number(self):
        expected_result = [1, 2, 4, 3]
        self.integer_list.insert(2, 4)
        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_insert_on_index_out_of_range_expected_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(10, 4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_no_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(2, 3.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_getting_biggest_value_expect_success(self):
        expected_result = 3
        actual_result = self.integer_list.get_biggest()
        self.assertEqual(expected_result, actual_result)

    def test_get_index_expect_success(self):
        expected_result = 0
        actual_result = self.integer_list.get_index(1)

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
