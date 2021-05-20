from unittest import TestCase
import classroom_manager


class test_classroom(TestCase):
    def test___init__(self):
        #function that is used to verify that the init function values are equal
        student = classroom_manager.Student(12, "Joe", "Smith")
        #ass = []
        self.assertEqual("Joe", student.first_name)
        self.assertEqual("Smith", student.last_name)
        self.assertEqual(12, student.id)
        #self.assertEqual()
    def test_get_full_name(self):
        student = classroom_manager.Student(12, "Joe", "Smith")
        fn = student.first_name
        ln = student.last_name
        fullname = classroom_manager.Student.get_full_name(student)
        self.assertEqual(fullname, (fn + " " + ln))
        #assert False

    def test_submit_assignment(self):
        student = classroom_manager.Student(12, "Joe", "Smith")
        student.assignments = []
        student.assignments.append("test")
        assname = classroom_manager.Assignment("test", 100)
        student.get_assignments()
        name = student.get_assignment("test")
        student.submit_assignment(name)
        self.assertEqual(len(student.assignments), 2)
        #assArray = []
        #self.assertTrue(len(subass) > 0)
        #self.assertEqual(subass, 2)
        #asss = [ass]
        #assert False

    def test_get_assignments(self):
        student = classroom_manager.Student(12, "Joe", "Smith")
        asstest = classroom_manager.Assignment("test", 100)
        student.submit_assignment(asstest)
        #student.assignments.append("test")
        ga = student.get_assignments()
        self.assertEqual(ga, asstest)
        #assert False

    def test_get_assignment(self):
        student = classroom_manager.Student(12, "Joe", "Smith")
        asstest = classroom_manager.Assignment("test", 100)
        student.submit_assignment(asstest)
        #student.assignments.append(test)
        ga = student.get_assignment(asstest)
        self.assertEqual(ga, asstest)
        #assert False

    def test_get_average(self):
        student = classroom_manager.Student(12, "Joe", "Smith")
        grades = 0
        #ga = student.get_assignments()
        assgrade1 = classroom_manager.Assignment("test", 100)
        assgrade2 = classroom_manager.Assignment("test2", 100)

        grades = assgrade1.assign_grade(88)
        grade2 = assgrade2.assign_grade(83)
        gradesum = assgrade1.grade + assgrade2.grade
        testavg = gradesum/2
        student.assignments.append(assgrade1)
        student.assignments.append(assgrade2)
        for a in student.assignments:
            print(a)
        avg = student.get_average()
        self.assertEqual(testavg, avg)
        #assert False

    def test_remove_assignment(self):
        student = classroom_manager.Student(12, "Joe", "Smith")
        student.assignments = []
        ass = classroom_manager.Assignment("test", 100)
        student.assignments.append(ass)
        student.remove_assignment(ass)
        self.assertEqual(len(student.assignments), 0)
        #assert False


class assignmenttest(TestCase):
    def test___init__(self):
        #function that is used to verify that the init function values are equal
        ass = classroom_manager.Assignment("test", 100)
        ass.grade = 88
        self.assertEqual("test", ass.name)
        self.assertEqual(100, ass.max_score)
        self.assertEqual(88, ass.grade)
    def test_assign_grade(self):
        grade = 0
        ass = classroom_manager.Assignment("test", 100)
        ass.assign_grade(88)
        #if ass.grade > ass.max_score:
         #   ass.grade = None
        self.assertEqual(88, ass.grade)
        ass.assign_grade(111)
        self.assertEqual(None, ass.grade)
        #assert False