class Cars():
        def __init__(self,model,renk,silindir):
            print("init fonk. çağırıldı.")
            self.model=model
            self.renk=renk
            self.silindir=silindir

car = Cars("Kangoo","Gümüş",4)
car1 = Cars("TOGG","Beyaz",8)
print(car.model)
print(car1.model)
print(car.silindir)
print(car1.silindir)