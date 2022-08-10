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
        schoolObj.add_student("Furkan")
        schoolObj.add_room("1111")
        schoolObj.add_room("1112")
        schoolObj.add_room("1212")
        schoolObj.add_room("1211")
        schoolObj.add_room("1309")
        schoolObj.add_admin("TÜRK")
        schoolObj.add_admin("EMRE")
        schoolObj.add_lesson(LesseonType.FIZIK)
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








