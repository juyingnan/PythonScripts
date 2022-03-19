#!/usr/bin/python

# Yue Chen

class course():
    def __init__(self, title, course_times, location):
        self.title = title
        self.course_times = course_times
        self.students = []
        self.student_number = self.students.__len__()
        self.location = location
        self.special_requirements = []
        self.language_info = None

    def set_title(self, title):
        self.title = title

    def set_location(self, location):
        self.location = location

    def set_course_times(self, course_times):
        self.course_times = course_times

    def add_student(self, student_name):
        self.students.append(student_name)
        self.student_number = self.students.__len__()

    def del_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            self.student_number = self.students.__len__()

    def add_special_requirement(self, special_requirement):
        if special_requirement not in self.special_requirements:
            self.special_requirements.append(special_requirement)

    def del_special_requirement(self, special_requirement):
        if special_requirement in self.special_requirements:
            self.special_requirements.remove(special_requirement)

    def set_language_info(self, language_taught, level_of_competence):
        self.language_info = language_info(language_taught, level_of_competence)
        self.add_special_requirement("multimedia room")

    def del_language_info(self):
        self.language_info = None
        self.del_special_requirement("multimedia room")

    def print_course_info(self):
        print "TITLE: ", self.title
        print "COURSE TIMES: ", self.course_times
        print "STUDENT NUMBER: ", self.student_number
        print "LOCATION: ", self.location
        if self.language_info:
            self.language_info.print_language_info()
        print "STUDENTS: ", self.students
        print "SPECIAL REQUIREMENTS", self.special_requirements

class language_info():
    def __init__(self, language_taught, level_of_competence):
        self.language_taught = language_taught
        self.level_of_competence = level_of_competence

    def set_language_taught(self, language_taught):
        self.language_taught = language_taught

    def set_level_of_competence(self, level_of_competence):
        self.level_of_competence = level_of_competence

    def print_language_info(self):
        print "LANGUAGE INFO:"
        print "\tLANGUAGE TAUGHT: ", self.language_taught
        print "\tLEVEL OF COMPETENCE: ", self.level_of_competence

# Test
english_course = course("English", 36, "AT-1-1")
english_course.print_course_info()
print "----------------------------"
english_course.set_course_times(24)
english_course.set_title("Advanced English")
english_course.set_location("AT-1-2")
english_course.add_student("Jack")
english_course.add_student("Jack")
english_course.add_student("Rose")
english_course.del_student("Jack")
english_course.del_student("James")
english_course.add_special_requirement("No drinking")
english_course.add_special_requirement("No drinking")
english_course.del_special_requirement("No drinking")
english_course.del_special_requirement("No eating")
english_course.set_language_info("English", "III")
english_course.print_course_info()
print "----------------------------"
english_course.del_language_info()
english_course.print_course_info()
