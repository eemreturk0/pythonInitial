class Yazılımcı():
    def __init__(self,isim,soyisim,numara,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.diller=diller

    def bilgileriGöster(self):
        print("""
              Yazılımcı özellikleri
              
              isim : {}
              soyisim : {}
              numara : {}
              Diller : {}
              
              
              """.format(self.isim,self.soyisim,self.numara,self.diller))

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor...")
        self.diller.append(yeni_dil)

yazılımcı = Yazılımcı("Emre","TÜRK",1453,["Python","C","C++"])

yazılımcı.dil_ekle("php")

print(yazılımcı.bilgileriGöster())
