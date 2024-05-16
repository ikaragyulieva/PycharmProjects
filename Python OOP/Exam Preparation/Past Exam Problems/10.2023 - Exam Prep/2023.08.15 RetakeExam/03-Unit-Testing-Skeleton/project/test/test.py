from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(14500.50, 2, True)

    def test_init(self):
        self.assertEqual(14500.50, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)

        self.assertIsInstance(self.trip.budget, float)
        self.assertIsInstance(self.trip.travelers, int)
        self.assertIsInstance(self.trip.is_family, bool)
        self.assertIsInstance(self.trip.booked_destinations_paid_amounts, dict)

    def test_not_valid_traveller_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip_test = Trip(14500.50, -2, True)

        self.assertEqual('At least one traveler is required!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.trip_test = Trip(14500.50, 0, True)

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_one_traveler_family_true_expect_family_turns_false(self):
        self.trip_test = Trip(14500.50, 1, True)

        self.assertEqual(False, self.trip_test.is_family)

    def test_more_travelers_family_false(self):
        self.trip_test = Trip(14500.50, 4, False)

        self.assertEqual(False, self.trip_test.is_family)

    def test_book_trip_destination_not_offered_expect_string_message(self):
        result = self.trip.book_a_trip("Spain")

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_trip_not_enough_budget(self):
        self.trip.budget = 1000
        result = self.trip.book_a_trip("Australia")

        self.assertEqual('Your budget is not enough!', result)

    def test_book_trip_enough_budget_family(self):
        self.trip.budget = 900
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 0.00', result)

    def test_book_trip_enough_budget(self):
        self.trip.is_family = False
        result = self.trip.book_a_trip("Australia")
        self.assertEqual(3100.50, self.trip.budget)
        self.assertEqual({"Australia": 11400}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(f'Successfully booked destination Australia! Your budget left is 3100.50', result)

    def test_booking_status_no_bookings(self):
        result = self.trip.booking_status()

        self.assertEqual('No bookings yet. Budget: 14500.50', result)

    def test_booking_status_with_bookings(self):
        self.trip.booked_destinations_paid_amounts = {"Australia": 10260, "Bulgaria": 900, }
        result = self.trip.booking_status()

        self.assertEqual("Booked Destination: Australia\n"
                         "Paid Amount: 10260.00\n"
                         "Booked Destination: Bulgaria\n"
                         "Paid Amount: 900.00\n"
                         "Number of Travelers: 2\n"
                         "Budget Left: 14500.50", result)


if __name__ == "__main__":
    main()
