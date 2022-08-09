import time

from emre.school.model import*
def startFunction():
    print("**************")
    print()
    print("\t School System \t")
    print()
    print("**************")

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
        schoolObj.add_room("bilgisayar")
        schoolObj.add_admin("TÜRK")
        schoolObj.add_admin("EMRE")
        print("School")
        print(schoolObj)
        print(schoolObj.admin_list)








