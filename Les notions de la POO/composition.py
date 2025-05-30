# La composition est un moyen d'agréger des objets en faisant de certains objets des attributs d'autres objets.

# Quelques exemples d'agrégation et de composition

class Student:
    def __init__(self, name, surname, student_number):
        self.name = name
        self.surname = surname
        self.student_number = student_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {} 

    def add_course(self, description, course_code, credit):
        course = Course(description, course_code, credit, self)
        self.courses[course_code] = course
        return course


class Course:
    def __init__(self, description, course_code, credit, department):
        self.description = description
        self.course_code = course_code
        self.credit = credit
        self.department = department
        self.running = []

    def add_running(self, year):
        run = CourseRunning(self, year)
        self.running.append(run)
        return run


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student) 


# Exemple d'utilisation
maths_dept = Department("Mathematics and Applied Mathematics", "MAM")

mam100w = maths_dept.add_course("Mathematics 100", "MAM100W", 1)
mam100w_2013 = mam100w.add_running(2013)  

bob = Student("Bob", "Smith", "S123")  
bob.enrol(mam100w_2013)