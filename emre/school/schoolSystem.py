import time

from emre.school.model import *
from emre.school.printer import *


def startFunction():
    printPurple("**************")
    print()
    printPurple("\t School System \t")
    print()
    printPurple("**************")


def Menu():
    while True:
        try:
            printText("""\n 
    1-) Main Menu
    2-) Student Menu
    3-) Teacher Menu
    4-) Lesson Menu
    0-) çıkış için""")
            answer = int(input(""))
            if answer in [1, 2, 3, 4, 0]:
                return answer
            else:
                printError("1 2 3 4 0 olabilir")
        except:
            printError("Girdiğiniz Şey Sayı olmalıdır ")


def Menu_main():
    while True:
        try:
            printText("""\n 
   1-)Tüm Öğrencileri Gör
   2-)Tüm Öğretmenleri Gör
   3-)Tüm Sınıfları Gör
   4-)Tüm Dersleri Gör
   0-) Menuye donmek için 0 a bas""")
            answer = int(input(""))
            if answer in [1, 2, 3, 4, 0]:
                return answer
            else:
                printError("1 2 3 4 0 olabilir")
        except:
            printError("Girdiğiniz Şey Sayı olmalıdır ")

def Student_menu():
    while True:
        try:
            printText("""\n 
    1-)Öğrenci ekle
    2-)Öğrenci sil
    3-)Öğrenci ara
    4-)Derse öğrenci ekle
    5-)Dersten öğrenci çıkar
    0-) Menuye donmek için 0 a bas""")
            answer = int(input(""))
            if answer in [1, 2, 3, 4, 5, 0]:
                return answer
            else:
                printError("1 2 3 4 5 0 olabilir")
        except:
            printError("Girdiğiniz Şey Sayı olmalıdır ")

def Teacher_menu():
    while True:
        try:
            printText("""\n 
    1-)Öğretmen ekle
    2-)Öğretmen sil
    3-)Öğretmeni derse ekle
    4-)Öğretmeni dersten çıkar
    0-) Menuye donmek için 0 a bas""")
            answer = int(input(""))
            if answer in [1, 2, 3, 4, 0]:
                return answer
            else:
                printError("1 2 3 4  0 olabilir")
        except:
            printError("Girdiğiniz Şey Sayı olmalıdır ")

def Lesson_menu():
    while True:
        try:
            printText("""\n 
    1-)Bütün dersleri yazdır
    2-)Ders tipine göre göster
    0-) Menuye donmek için 0 a bas""")
            answer = int(input(""))
            if answer in [1, 2, 0]:
                return answer
            else:
                printError("1 2 0 olabilir")
        except:
            printError("Girdiğiniz Şey Sayı olmalıdır ")


def teacher_type(text: str) -> LesseonType:
    while True:
        try:
            comingText = input(text).lower()
            if comingText == "f" or comingText == "FIZIK":
                return LesseonType.FIZIK
            elif comingText == "k" or comingText == "KIMYA":
                return  LesseonType.KIMYA
            elif comingText == "m" or comingText == "MATH":
                return  LesseonType.MATH
            else:
                printError("FIZIK , KIMYA, MATH OLMAK ZORUNDA")
        except:
            printError("Girdiğiniz değer f,k,m FIZIK,KIMYA,MAT olmak zorunda.")


def add_student_to_lesson_fromterminal():
    while True:
        try :
            print(schoolObj.list_writer("student"))
            studentNumber = int(input("student number yazınız :"))
            print(schoolObj.list_writer("lesson"))
            lessonNumber = int(input("lesson number yazınız :"))
            schoolObj.add_student_to_lesson(schoolObj.student_list[studentNumber], schoolObj.lesson_list[lessonNumber])
            printPurple("Başaraıyla eklendi.")
            print(schoolObj.student_list)
            break
        except:
            printError("listedeki numara girilmeli")


def add_teacher_to_lesson_fromterminal():
    while True:
        try :
            print(schoolObj.list_writer("lesson"))
            lessonNumber = int(input("lesson number yazınız :"))
            print(schoolObj.list_writer("teacher"))
            teacherNumber = int(input("teacher number yazınız :"))
            schoolObj.add_lesson_to_teacher(schoolObj.lesson_list[lessonNumber], schoolObj.teacher_list[teacherNumber])
            print(schoolObj.teacher_list)
            printPurple("Başaraıyla eklendi.")
            break
        except:
            printError("listedeki numara girilmeli")


def del_student_to_lesson_fromterminal():
    while True:
        try :
            print(schoolObj.list_writer("student"))
            studentNumber = int(input("student number yazınız :"))
            print(schoolObj.list_writer("lesson"))
            lessonNumber = int(input("lesson number yazınız :"))
            schoolObj.del_student_to_lesson(schoolObj.student_list[studentNumber], schoolObj.lesson_list[lessonNumber])
            print(schoolObj.student_list)
            printPurple("Başaraıyla silindi.")
            break
        except:
            printError("listeden numara girilmeli")


def dell_teacher_to_lesson_fromterminal():
    while True:
        try :
            print(schoolObj.list_writer("teacher"))
            teacherNumber = int(input("teacher number yazınız :"))
            print(schoolObj.list_writer("lesson"))
            lessonNumber = int(input("lesson number giriniz :"))
            schoolObj.del_lesson_to_teacher(schoolObj.teacher_list[teacherNumber], schoolObj.lesson_list[lessonNumber])
            print(schoolObj.teacher_list)
            printPurple("Başaraıyla silindi.")
            break
        except:
            printError("listeden numara girilmeli.")


if __name__ == "__main__":

    print(startFunction())
    schoolObj = School("Ebyu")
    adminObj = Admin("Emre")
    schoolObj.admin = adminObj
    schoolObj.add_teacher("Cihat", LesseonType.MATH)
    schoolObj.add_teacher("Tufi", LesseonType.FIZIK)
    schoolObj.add_teacher("Fatih", LesseonType.KIMYA)
    schoolObj.add_student("Furkan")
    schoolObj.add_student("Nur")
    schoolObj.add_student("Ali")
    schoolObj.add_admin("EMRE")
    schoolObj.add_room("PC1")
    schoolObj.add_room("PC2")
    schoolObj.add_room("PC3")
    schoolObj.add_lesson(LesseonType.FIZIK, "FZ101")
    schoolObj.add_lesson(LesseonType.FIZIK, "FZ102")
    schoolObj.add_lesson(LesseonType.KIMYA, "KM101")
    schoolObj.add_lesson(LesseonType.KIMYA, "KM102")
    schoolObj.add_lesson(LesseonType.MATH, "MT101")
    schoolObj.add_lesson(LesseonType.MATH, "MT102")
    schoolObj.add_lesson(LesseonType.ING, "I101")
    schoolObj.add_lesson(LesseonType.TURKCE, "TU101")
    schoolObj.add_lesson(LesseonType.TARIH, "TAR101")
    School.add_lesson_to_room(schoolObj.lesson_list[0], schoolObj.room_list[0])  # classmethod çağrısı yaptık
    School.add_lesson_to_room(schoolObj.lesson_list[1], schoolObj.room_list[1])
    School.add_lesson_to_room(schoolObj.lesson_list[2], schoolObj.room_list[2])
    School.add_lesson_to_teacher(schoolObj.lesson_list[0], schoolObj.teacher_list[1])
    School.add_lesson_to_teacher(schoolObj.lesson_list[1], schoolObj.teacher_list[2])
    School.add_lesson_to_teacher(schoolObj.lesson_list[2], schoolObj.teacher_list[0])
    School.add_student_to_lesson(schoolObj.student_list[0], schoolObj.lesson_list[0])
    School.add_student_to_lesson(schoolObj.student_list[1], schoolObj.lesson_list[1])
    School.add_student_to_lesson(schoolObj.student_list[1], schoolObj.lesson_list[0])
    School.add_student_to_lesson(schoolObj.student_list[2], schoolObj.lesson_list[2])
    printWARNING("School")
    # print(schoolObj)
    # printPurple("TEACHER LİST")
    # print(schoolObj.teacher_list)
    # printPurple("ROOM LİST")
    # print(schoolObj.room_list)
    # printPurple("STUDENT LİST")
    # print(schoolObj.student_list)
    # printPurple("ADMİN LİST")
    # print(schoolObj.admin_list)
    # printPurple("LESSON LİST")
    # print(schoolObj.lesson_list)
    # schoolObj.student_list[1].writer()
    #print(schoolObj.filter("student","ur"))
    while True:
        cevap = Menu()
        if cevap == 1:

            while True:
                cevap = Menu_main()

                if cevap == 1:
                    schoolObj.list_writer("student")
                elif cevap == 2:
                    schoolObj.list_writer("teacher")
                elif cevap == 3:
                    schoolObj.list_writer("room")
                elif cevap == 4:
                    schoolObj.list_writer("lesson")
                elif cevap == 0:
                    break
        elif cevap ==2:
            while True:
                cevap=Student_menu()

                if cevap == 1:
                    ad = input("ögrenci adi:")
                    schoolObj.add_student(ad)
                    print(schoolObj.list_writer("student"))
                elif cevap == 2:
                    print(schoolObj.list_writer("student"))
                    numberValue = int(input("numara giriniz :"))
                    schoolObj.del_student(numberValue)
                    print(schoolObj.list_writer("student"))
                elif cevap == 3:
                    filt = schoolObj.filter("student",input("aranıcak harfleri girin:"))
                    print(filt)
                elif cevap == 4:
                    add_student_to_lesson_fromterminal()
                elif cevap == 5:
                    del_student_to_lesson_fromterminal()
                elif cevap == 0:
                    break
        elif cevap == 3:
            while True:
                cevap =Teacher_menu()
                if cevap == 1:
                    print(schoolObj.list_writer("teacher"))
                    ad = input("öğretmen adı:")
                    type = teacher_type("dersin kodu")
                    schoolObj.add_teacher(ad,type)
                    print(schoolObj.list_writer("teacher"))
                    print(schoolObj.teacher_list)
                elif cevap ==2:
                    print(schoolObj.list_writer("teacher"))
                    numberValueTeacher = int(input("numara giriniz :"))
                    schoolObj.del_teacher(numberValueTeacher)
                    print(schoolObj.list_writer("teacher"))
                elif cevap == 3:
                    add_teacher_to_lesson_fromterminal()
                    print(schoolObj.teacher_list)
                elif cevap == 4:
                    dell_teacher_to_lesson_fromterminal()
                elif cevap == 0:
                    break
        elif cevap == 4:
            while True:
                cevap = Lesson_menu()
                if cevap ==1:
                    schoolObj.list_writer("lesson")
                if cevap ==2:
                    schoolObj.lesson_writer("lesson")
                    filt = schoolObj.lesson_filter("lesson",input("aranıcak kodu giriniz:"))
                    print(filt)
                if cevap== 0:
                    break

        elif cevap == 0:
            printPurple("system sonlandırılıyor..")
            break
