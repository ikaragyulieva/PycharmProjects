from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):

    def setUp(self) -> None:
        self.student = StudentReportCard("James", 2)

    def test_init(self):
        self.assertEqual("James", self.student.student_name)
        self.assertEqual(2, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_init_no_student_name_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_student = StudentReportCard("", 3)

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_init_incorrect_school_year_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_student = StudentReportCard("John", 20)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test_student = StudentReportCard("Jenny", -3)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_value_definition(self):
        self.assertIsInstance(self.student.student_name, str)
        self.assertIsInstance(self.student.school_year, int)
        self.assertIsInstance(self.student.grades_by_subject, dict)

    def test_add_grade_existing_subject(self):
        self.student.grades_by_subject = {"Python": [10], "C#": [8], "Agile": [9]}
        self.student.add_grade("Python", 9.5)

        self.assertEqual({"Python": [10, 9.5], "C#": [8], "Agile": [9]}, self.student.grades_by_subject)

    def test_add_grade_no_existing_subject(self):
        self.student.grades_by_subject = {"C#": [8], "Agile": [9]}
        self.student.add_grade("Python", 9.5)

        self.assertEqual({"C#": [8], "Agile": [9], "Python": [9.5]}, self.student.grades_by_subject)

    def test_average_grade_by_subject_expect_string(self):
        self.student.grades_by_subject = {"Python": [10, 8.2], "C#": [8.5, 7], "Agile": [9.4, 10]}
        result = self.student.average_grade_by_subject()

        self.assertEqual("Python: 9.10\nC#: 7.75\nAgile: 9.70", result)

    def test_average_grade_for_all_subjects_expect_string(self):
        self.student.grades_by_subject = {"Python": [10, 8.2], "C#": [8.5, 7], "Agile": [9.4, 10]}
        result = self.student.average_grade_for_all_subjects()

        self.assertEqual("Average Grade: 8.85", result)

    def test_represent(self):
        self.student.grades_by_subject = {"Python": [10, 8.2], "C#": [8.5, 7], "Agile": [9.4, 10]}
        result = self.student.__repr__()

        self.assertEqual(
            "Name: James\n"
            "Year: 2\n"
            "----------\n"
            "Python: 9.10\n"
            "C#: 7.75\n"
            "Agile: 9.70\n"
            "----------\n"
            "Average Grade: 8.85",
            result
        )


if __name__ == "__main__":
    main()
