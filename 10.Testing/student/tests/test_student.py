from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    STUDENT_NAME = 'John'

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_initialization_without_courses(self):
        self.setUp()
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_initialization_with_courses(self):
        courses = {'Python OOP': ['note', 'note1', 'note2']}
        student = Student(self.STUDENT_NAME, courses)

        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(student.courses, courses)

    def test_enroll_returns_message_notes_have_been_updated(self):
        course_name = 'Python OOP'
        courses = {course_name: ['lab1', 'lab2', 'lab3']}

        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ['lab4', 'lab5'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['lab1', 'lab2', 'lab3', 'lab4', 'lab5'], student.courses[course_name])

    def test_enroll_returns_message_course_and_notes_have_been_added(self):
        self.setUp()
        result = self.student.enroll('Python OOP', ['lab1', 'lab2', 'lab3'])
        message = "Course and course notes have been added."

        self.assertEqual(result, message)
        self.assertTrue('Python OOP' in self.student.courses)
        self.assertEqual(['lab1', 'lab2', 'lab3'], self.student.courses['Python OOP'])

    def test_enroll_returns_message_course_and_notes_have_been_added_with_y(self):
        self.setUp()
        result = self.student.enroll('Python OOP', ['lab1', 'lab2', 'lab3'], 'Y')
        message = "Course and course notes have been added."

        self.assertEqual(result, message)
        self.assertTrue('Python OOP' in self.student.courses)
        self.assertEqual(['lab1', 'lab2', 'lab3'], self.student.courses['Python OOP'])

    def test_enroll_returns_message_course_has_been_added(self):
        self.setUp()
        self.student.courses = {}
        result = self.student.enroll('Python OOP', ['lab1', 'lab2', 'lab3'], 'ala bala')
        message = "Course has been added."

        self.assertEqual(result, message)
        self.assertTrue('Python OOP' in self.student.courses)
        self.assertEqual([], self.student.courses['Python OOP'])

    def test_add_notes_return_message_notes_have_been_update(self):
        self.setUp()
        self.student.courses = {'Python OOP': [], 'JS': [], 'Java': []}
        result = self.student.add_notes('Python OOP', "Bulgaria is the Silicon Valley of Europe")
        message = "Notes have been updated"

        self.assertEqual(result, message)
        self.assertEqual(self.student.courses['Python OOP'], ["Bulgaria is the Silicon Valley of Europe"])

    def test_add_notes_raise_error(self):
        self.setUp()
        self.student.courses = {'Python OOP': [], 'JS': [], 'Java': []}
        message = "Cannot add notes. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student.add_notes('PHP', 'This course is not in our data')
        self.assertEqual(message, str(ex.exception))

    def test_remove_course_return_message_course_has_been_removed(self):
        self.setUp()
        self.student.courses = {'Python OOP': [], 'JS': [], 'Java': []}
        message = "Course has been removed"

        result = self.student.leave_course('Java')
        self.assertEqual(result, message)
        self.assertEqual(self.student.courses, {'Python OOP': [], 'JS': []})

    def test_remove_course_raise_error_when_course_not_found(self):
        self.setUp()
        self.student.courses = {'Python OOP': [], 'JS': [], 'Java': []}
        message = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('PHP')
        self.assertEqual(message, str(ex.exception))







if __name__ == '__main__':
    main()
