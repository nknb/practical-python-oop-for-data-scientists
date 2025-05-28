# la composition est un moyen d'agréger des objets en faisant de certains objets des attributs d'dautre object.

# quelque exempled d'agregation et de composition

class Student:
    def __init__(self , name , surname , student_number):
        self.name = name
        self.surname = surname
        self.student_number = student_number
        self.classes = []
        
    def enrol(self, course_runing):
        self.classes.append(course_runing)
        course_runing.add_student(self)

class Departement:
    def __init__(self , name , departement_code):
        self.name = name
        self.departement_code = departement_code
        self.sourses = {}
    