import time
import random
import enum
import jsonpickle

from emre.school.fileManager import writeToFile
from emre.school.printer import printList
import json
import jsonpickle

class PeopleType(enum.Enum):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3


class LesseonType(enum.Enum):
    MATH = 1
    FIZIK = 2
    KIMYA = 3
    ING = 4
    TURKCE = 5
    TARIH = 6





class Lesson():
    def __init__(self, lesson_type: LesseonType, code: str):
        self.lesson_type = lesson_type
        self.code = code
        self.lessonRoom = None

    def get_student_list(self,school):
        sList = []
        for s in school.student_list:
            for l in s.lesson_list:
                if self.code == l.code and self.lesson_type == l.lesson_type:
                    sList.append(s)
                    break
        return  sList


    def get_teacher_list(self, school):
        tList = []
        for s in school.teacher_list:
            for l in s.lesson_list:
                if self.code == l.code and self.lesson_type == l.lesson_type:
                    tList.append(s)
                    break
        return  tList

    def __repr__(self):
        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()
    def get_name(self):
        return self.code+" "+self.lesson_type.name
    def writer(self):
            txt = "ders: {ders} code: {code}"
            print(txt.format(ders=self.lesson_type.name, code=self.code))




class Room():
    def __init__(self, room_name):
        self.room_name = room_name

    def get_lesson_list(self,school):
        rList = []
        for l in school.lesson_list:
            if l.lessonRoom.room_name== self.room_name:
                rList.append(l)
                break
        return rList
    def __repr__(self):
        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()
    def writer(self):
        txt = "sinif: {sinif} "
        print(txt.format(sinif=self.room_name))

class People:
    def __init__(self, name, type: PeopleType):
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
    def __init__(self, name, lesson_type: LesseonType):
        super().__init__(name, PeopleType.TEACHER)
        print("Teacher sınıfının init fonksiyonu")
        self.lesson_type = lesson_type
        self.lesson_list = []

    def __repr__(self):
        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()
    def writer(self):
        txt = "ogretmen: {ogretmen} "
        print(txt.format(ogretmen=self.name))

class Student(People):
    def __init__(self, name, number: int):
        super().__init__(name, PeopleType.STUDENT)
        self.lesson_list = []
        self.number = number

    def __repr__(self):
        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()
    def writer(self):
        txt = "ogrenci: {ogrenci}"
        print(txt.format(ogrenci=self.name))

    def stWriter(self):
        txt = "ogrenci: {ogrenci} ders: {ders}"
        print(txt.format(ogrenci=self.name,ders=self.lesson_list))



class School:
    def __init__(self, name: str):
        self.name = name
        self.admin = None
        self.student_list = []
        self.teacher_list = []
        self.room_list = []
        self.lesson_list = []
        self.admin_list = []




    def filter(self,value,filter):
        returnlist = []
        if (value == "student"):
            for s in self.student_list:
                if filter in s.name:
                    returnlist.append(s)

        elif (value == "lesson"):
            for l in self.lesson_list:
                if filter in l.code:
                    returnlist.append(l)
        return returnlist

        #elif (value == "teacher"):
            #for t in self.teacher_list:
                #t.writer()
        #elif (value == "room"):
            #for r in self.room_list:
                #r.writer()
       # elif (value == "lesson"):
            #for l in self.lesson_list:
             #   l.writer()

    def del_student(self, studentNumber: int):
        number = 0
        sObj = self.student_list[studentNumber]
        self.student_list.remove(sObj)
        writeToFile(self)

    def del_teacher(self, teacherNumber: int):
        number = 0
        tObj = self.teacher_list[teacherNumber]
        self.teacher_list.remove(tObj)
        writeToFile(self)


    def add_student(self, student_name: str):
        print("adding students...")

        control = False
        number = 0
        while not control:
            control = True
            number = random.randint(1, 1000)
            for st in self.student_list:
                if (st.number == number):
                    control = False
                    break

        student = Student(student_name, number)

        self.student_list.append(student)
        print("successful..")
        writeToFile(self)

    def __repr__(self):

        return self.__dict__.__str__()

    def __str__(self):
        return self.__repr__()

    def add_teacher(self, teacher_name: str, lesson: LesseonType):
        print("\nadding teacher...")

        teacherObj = Teacher(teacher_name, lesson)

        self.teacher_list.append(teacherObj)
        print("successful..")
        writeToFile(self)
    def add_room(self, room_name: str):
        print("\nadding room...")

        room = Room(room_name)

        self.room_list.append(room)
        print("successful..")
        writeToFile(self)
    def add_admin(self, admin_name: str):
        print("\nadding admin user...")

        admin = Admin(admin_name)

        self.admin_list.append(admin)
        print("successful..")
        writeToFile(self)
    def add_lesson(self, lesson_type: LesseonType, code: str):
        """
        :param lesson_type:
        :param code:
        :return:
        """
        print("\nadding lesson...")
        lessonObj = Lesson(lesson_type, code)
        self.lesson_list.append(lessonObj)
        print("successful..")
        writeToFile(self)
    @classmethod
    def add_lesson_to_room(cls, lessonObj: Lesson, roomObj: Room):
        """
        Bu kod Lessona Room ekler aynı zamanda Roomun lessonlistesine lesson ekler.
        :param lessonObj: eklenecek ders
        :param roomObj: eklenecek sınıf
        :return:
        """

        lessonObj.lessonRoom = roomObj

    @classmethod
    def add_lesson_to_teacher(cls, lessonObj: Lesson, teacherObj:Teacher):


        teacherObj.lesson_list.append(lessonObj)
    @classmethod
    def del_lesson_to_teacher(cls, teacherObj: Teacher, lessonObj: Lesson):
        teacherObj.lesson_list.remove(lessonObj)


    @classmethod
    def add_student_to_lesson(cls,studentObj: Student, lessonObj: Lesson):

        studentObj.lesson_list.append(lessonObj)

    @classmethod
    def del_student_to_lesson(cls,studentObj: Student, lessonObj: Lesson):
        studentObj.lesson_list.remove(lessonObj)







