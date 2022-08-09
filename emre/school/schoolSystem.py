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
    islem = input("İşlemi seçiniz:")

    if (islem == "x"):
        print("School System sonlanlandırılıyor...")


    elif (islem == "1"):
        student_name = input("İsimleri ',' ile ayırarak girin")

        student_list = student_name.split(",")
        for eklenecekler in student_list:
            People.add_Student(eklenecekler)
    else:
        print("Geçersiz işlem....")


if __name__ == "__main__":

        schoolObj = School("Ebyu")
        adminObj = Admin("Emre")
        schoolObj.admin=adminObj
        schoolObj.add_teacher("Cihat",LesseonType.MATH)
        schoolObj.add_student("Furkan")
        schoolObj.add_room("bilgisayar")
        print("School")
        print(schoolObj)







