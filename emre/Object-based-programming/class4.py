class Calisan():
    def __init__(self,isim,maas,departman):
        print("calışan sınıfının init fonksiyonu.")

        self.isim=isim
        self.maas=maas
        self.departman=departman

    def bilgileriGöster(self):
        print("Çalışan sınıfın bilgileri : ")
        print(" isim : {}\n maas : {}\n departman : {}\n".format(self.isim,self.maas,self.departman))

    def departman_degis(self,yeni_departman):
        self.departman=yeni_departman

class Yönetici(Calisan):
    pass

yonetici= Yönetici("Emre TÜRK",3000,"PC")
yonetici.departman_degis("PC HİZMETLERİ")

print(dir(yonetici))

print(yonetici.isim,yonetici.maas,yonetici.departman)


