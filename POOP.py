class Dog:
    def __init__(self,name,age):  #spetsiaalne meetod. uue objekti loomisel kutsutakse kohe välja init meetodis defineeritud paramaeetritega
        self.name = name
        self.age = age#atribuut nimega name
        #print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("Tim",10)
d.set_age(8)
#d2 = Dog("Pontu",3)
print(d.name,d.age)  #prindin objekti atribuudid 'name'
#print(d2.get_name(),get_age())  #kutsun välja klassi Dog meetodi get_name objekti d2 jaoks

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # võin luua atribuudi, mida ei ole klassi init meetodis

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Raiko", 44, 95)  # klassi Student objektid atribuutidega name, age, grade
s2 = Student("Taibu", 20, 99)
s3 = Student("Timbu",23,90)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
#print(course.students[0].name)  # prindime objekti students[0] atribuudi name
print(course.get_average_grade())


"""
klassi __init__ meetod kutsutakse välja kohe kui klassi abil luuakse uus objekt
klassi sees võin luua atribuute, mida ei ole __init__ meetodis
"""