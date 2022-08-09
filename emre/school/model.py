import time
import random
import enum


class PeopleType(enum.Enum):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3


class LesseonType(enum.Enum):
    MATH = 1
    FIZIK = 2
    KIMYA = 3



class Lesson():
    def __init__(self, lesson_type:LesseonType):
        self.lesson_type = lesson_type
        self.teacher = None
        self.student_list = []
        self.room = None

class Room():
    def __init__(self,name):
        self.name = name
        self.lesson_list = []

class School:
    def __init__(self, name:str):
        self.name = name
        self.admin = None
        self.student_list = []
        self.teacher_list = []
        self.room_list = []
        self.lesson_list = []

    def add_student(self, student_name:str):
        print("adding students...")
        time.sleep(1)
        control = False
        number = 0
        while not control:
            control = True
            number = random.randint(1,1000)
            for st in self.student_list:
                if(st.number == number):
                    control = False
                    break

        student = Student(student_name,number)

        self.student_list.append(student)
        print("successful..")
    def __repr__(self):

        return self.__dict__.__str__()
        #return "name:%s admin:%d student:%s teacher:%d room:%d lesson:%d " % (self.name, self.admin, self.student_list, self.teacher_list, self.room_list,self.lesson_list)

    def __str__(self):
        return self.__repr__()

    def add_teacher(self, teacher_name:str,lesson:LesseonType):
        print("adding teacher...")
        time.sleep(1)
        teacher = Teacher(teacher_name,lesson)

        self.teacher_list.append(teacher)
        print("successful..")


class People:
    def __init__(self, name, type:PeopleType):
        print("People sınıfının init fonksiyonu")

        self.name = name
        self.type = type

    def peopleBilgiSystem(self):
        print("people bilgi system..")

        print("Name : {}\nType : {}\n".format(self.name, self.type))


class Admin(People):
    def __init__(self, name):
        super().__init__(name, PeopleType.ADMIN)

    def level_degis(self, new_level):
        self.level = new_level
    def __repr__(self):

        return self.__dict__.__str__()


    def __str__(self):
        return self.__repr__()

class Teacher(People):
    def __init__(self, name, lesson:LesseonType):
        super().__init__(name, PeopleType.TEACHER)
        print("Teacher sınıfının init fonksiyonu")
        self.lesson = lesson

    def __repr__(self):
        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()

class Student(People):
    def __init__(self, name, number:int):
        super().__init__(name, PeopleType.STUDENT)
        self.lesson_list = []
        self.number = number

    def __repr__(self):
        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()