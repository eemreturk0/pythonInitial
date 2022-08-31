import time

from emre.school.fileManager import *
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
            elif comingText == "i" or comingText == "ING":
                return  LesseonType.ING
            elif comingText == "t" or comingText == "TURKCE":
                return  LesseonType.TURKCE
            elif comingText == "ta" or comingText == "TARIH":
                return  LesseonType.TARIH
            else:
                printError("FIZIK , KIMYA, MATH, İNG, TURKCE, TARİH OLMAK ZORUNDA")
        except:
            printError("Girdiğiniz değer f,k,m,i,t,ta FIZIK,KIMYA,MAT,İNG,TURKCE,TARİH olmak zorunda.")


def add_student_to_lesson_fromterminal():
    while True:
        try :
            printList("student",schoolObj.student_list)
            studentNumber = int(input("student number yazınız :"))
            printList("lesson",schoolObj.lesson_list)
            lessonNumber = int(input("lesson number yazınız :"))
            schoolObj.add_student_to_lesson(schoolObj.student_list[studentNumber], schoolObj.lesson_list[lessonNumber])
            printPurple("Başaraıyla eklendi.")

            break
        except:
            printError("listedeki numara girilmeli")


def add_teacher_to_lesson_fromterminal():
    while True:
        try :
            printList("lesson",schoolObj.lesson_list)
            lessonNumber = int(input("lesson number yazınız :"))
            printList("teacher",schoolObj.teacher_list)
            teacherNumber = int(input("teacher number yazınız :"))
            schoolObj.add_lesson_to_teacher(schoolObj.lesson_list[lessonNumber], schoolObj.teacher_list[teacherNumber])

            printPurple("Başaraıyla eklendi.")
            break
        except:
            printError("listedeki numara girilmeli")


def del_student_to_lesson_fromterminal():
    while True:
        try :
            printList("student",schoolObj.student_list)
            studentNumber = int(input("student number yazınız :"))
            printList("lesson",schoolObj.lesson_list)
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
            printList("teacher",schoolObj.teacher_list)
            teacherNumber = int(input("teacher number yazınız :"))
            printList("lesson",schoolObj.lesson_list)
            lessonNumber = int(input("lesson number giriniz :"))
            schoolObj.del_lesson_to_teacher(schoolObj.teacher_list[teacherNumber], schoolObj.lesson_list[lessonNumber])
            print(schoolObj.teacher_list)
            printPurple("Başaraıyla silindi.")
            break
        except:
            printError("listeden numara girilmeli.")


if __name__ == "__main__":
    schoolObj = readFromFile()
    print(startFunction())
    if schoolObj == None:
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
        writeToFile(schoolObj)
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
                    printList("student", schoolObj.student_list)
                elif cevap == 2:
                    printList("teacher",schoolObj.teacher_list)
                elif cevap == 3:
                    printList("room",schoolObj.room_list)
                elif cevap == 4:
                    printList("lesson", schoolObj.lesson_list)
                elif cevap == 0:
                    break
        elif cevap ==2:
            while True:
                cevap=Student_menu()

                if cevap == 1:
                    ad = input("ögrenci adi:")
                    schoolObj.add_student(ad)
                    printList("student",schoolObj.student_list)
                elif cevap == 2:
                    printList("student",schoolObj.student_list)
                    numberValue = int(input("numara giriniz :"))
                    schoolObj.del_student(numberValue)
                    printList("student",schoolObj.student_list)
                elif cevap == 3:
                    filt = schoolObj.filter("student",input("aranıcak harfleri girin:"))
                    printList("student",filt)
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
                    printList("teacher",schoolObj.teacher_list)
                    ad = input("öğretmen adı:")
                    type = teacher_type("dersin kodu")
                    schoolObj.add_teacher(ad,type)
                    printList("teacher",schoolObj.teacher_list)
                    print(schoolObj.teacher_list)
                elif cevap ==2:
                    printList("teacher",schoolObj.teacher_list)
                    numberValueTeacher = int(input("numara giriniz :"))
                    schoolObj.del_teacher(numberValueTeacher)
                    printList("teacher",schoolObj.teacher_list)
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
                    printList("lesson",schoolObj.lesson_list)
                if cevap ==2:
                    printList("lesson",schoolObj.lesson_list)
                    filt = schoolObj.filter("lesson",input("aranıcak kodu giriniz:"))
                    printList("lesson",filt)
                if cevap== 0:
                    break

        elif cevap == 0:
            printPurple("system sonlandırılıyor..")
            break
