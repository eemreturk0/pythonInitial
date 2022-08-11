import time

from emre.school.model import*
from emre.school.printer import*
def startFunction():
    printPurple("**************")
    print()
    printPurple("\t School System \t")
    print()
    printPurple("**************")

def Menu():
    print("""
    1- Öğrenci ekle
    2- Öğrencileri göster
    3- Mevki değiştir
    4- Tüm bilgileri göster
    5- Çıkmak içi x ya basın
    
    """)

if __name__ == "__main__":
        print(startFunction())
        schoolObj = School("Ebyu")
        adminObj = Admin("Emre")
        schoolObj.admin=adminObj
        schoolObj.add_teacher("Cihat",LesseonType.MATH)
        schoolObj.add_teacher("Tufi",LesseonType.FIZIK)
        schoolObj.add_teacher("Fatih",LesseonType.KIMYA)
        schoolObj.add_student("Furkan")
        schoolObj.add_student("Nur")
        schoolObj.add_student("Ali")
        schoolObj.add_admin("EMRE")
        schoolObj.add_room("PC1")
        schoolObj.add_room("PC2")
        schoolObj.add_room("PC3")
        schoolObj.add_lesson(LesseonType.FIZIK,"FZ101")
        schoolObj.add_lesson(LesseonType.KIMYA,"KM102")
        schoolObj.add_lesson(LesseonType.MATH,"MT103")
        School.add_lesson_to_room(schoolObj.lesson_list[0], schoolObj.room_list[0])#classmethod çağrısı yaptık
        School.add_lesson_to_room(schoolObj.lesson_list[1], schoolObj.room_list[1])
        School.add_lesson_to_room(schoolObj.lesson_list[2], schoolObj.room_list[2])
        School.add_lesson_to_teacher(schoolObj.lesson_list[0], schoolObj.teacher_list[1])
        School.add_lesson_to_teacher(schoolObj.lesson_list[1], schoolObj.teacher_list[2])
        School.add_lesson_to_teacher(schoolObj.lesson_list[2], schoolObj.teacher_list[0])
        School.add_student_to_lesson(schoolObj.student_list[0],schoolObj.lesson_list[0])
        School.add_student_to_lesson(schoolObj.student_list[1],schoolObj.lesson_list[1])
        School.add_student_to_lesson(schoolObj.student_list[1],schoolObj.lesson_list[0])
        School.add_student_to_lesson(schoolObj.student_list[2],schoolObj.lesson_list[2])
        printWARNING("School")
        #print(schoolObj)
        printPurple("TEACHER LİST")
        print(schoolObj.teacher_list)
        printPurple("ROOM LİST")
        print(schoolObj.room_list)
        printPurple("STUDENT LİST")
        print(schoolObj.student_list)
        printPurple("ADMİN LİST")
        print(schoolObj.admin_list)
        printPurple("LESSON LİST")
        print(schoolObj.lesson_list)
        schoolObj.student_list[1].writer()









