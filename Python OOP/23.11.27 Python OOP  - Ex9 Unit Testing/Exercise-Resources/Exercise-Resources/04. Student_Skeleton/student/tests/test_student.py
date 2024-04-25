from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Anna")

    def test_init_without_courses(self):
        self.assertEqual("Anna", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        self.student_test = Student("Test", {"agile basics": ["test note", "new note 1", "new_note 2"]})
        self.assertEqual("Test", self.student_test.name)
        self.assertEqual({"agile basics": ["test note", "new note 1", "new_note 2"]}, self.student_test.courses)

    def test_enroll_already_taken_course_expect_string(self):
        self.student.courses["agile basics"] = ["test note"]
        expected_result_courses = {"agile basics": ["test note", "new note 1", "new_note 2"]}
        expected_result_return = self.student.enroll("agile basics", ["new note 1", "new_note 2"])

        self.assertEqual("Course already added. Notes have been updated.", expected_result_return)
        self.assertEqual(expected_result_courses, self.student.courses)

    def test_enrollment_with_course_note_y(self):
        # self.student.courses["agile basics"] = []
        result = self.student.enroll("agile basics", ["new note 1", "new_note 2"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"agile basics": ["new note 1", "new_note 2"]}, self.student.courses)

    def test_enrollment_with_empty_string(self):
        result = self.student.enroll("agile basics", ["new note 1", "new_note 2"], "")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"agile basics": ["new note 1", "new_note 2"]}, self.student.courses)

    def test_enrollment_add_course_expect_string_confirmation(self):
        result = self.student.enroll("agile basics", ["new note 1", "new_note 2"], "add")

        self.assertEqual("Course has been added.", result)
        self.assertEqual({"agile basics": []}, self.student.courses)

    def test_add_notes_to_no_existing_course_expect_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("agile_basics", ["new note 1", "new_note 2"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_note_to_existing_course_expect_string_confirmation(self):
        self.student.courses['agile basics'] = []
        result = self.student.add_notes('agile basics', "note 1")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"agile basics": ["note 1"]}, self.student.courses)

    def test_leave_not_existing_course_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("test course")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existing_course_expect_string_confirmation(self):
        self.student.courses = {'agile basics': []}
        result = self.student.leave_course('agile basics')

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)


if __name__ == "__main__":
    main()
