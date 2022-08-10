GRADEONE_RATE = 0.15
GRADETWO_RATE = 0.2
GRADETREE_RATE = 0.25
PROJECTGRADE_RATE = 0.4
class Student():
    def __init__(self,name:str,grade1:int,grade2:int,grade3,project_grade):
        self.name=name
        self.grade1=grade1
        self.grade2=grade2
        self.grade3=grade3
        self.project_grade=project_grade
        self.average = (grade1*GRADEONE_RATE + grade2*GRADETWO_RATE + grade3*GRADETREE_RATE + project_grade*PROJECTGRADE_RATE)

    def __repr__(self):
        return f"student:grade1:{self.grade1} grade2:{self.grade2} grade3:{self.grade3} project_grade:{self.project_grade} average:{self.average}"

    def __str__(self):
        return self.__repr__()
print("**************")
print()
print("\t Not Ortalaması Bulma Python \t")
print()
print("**************")
studentlist1 = []


def add_student():
    not1 = int(input("1.Notunuzu girin :"))
    not2 = int(input("2.Noutunuzu girin :"))
    not3 = int(input("3.Notunuzu girin :"))
    proje = int(input("Proje Notunuzu girin :"))
    student1 = Student("Emre", not1, not2, not3, proje)
    studentlist1.append(student1)

while True:
#dictinoary
    add_student()

    print("Öğrenciler : ",studentlist1)



#dillere göre yazım stillerini öğren hungarian,camelcase