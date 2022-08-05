# kullancıdan 1 sayı al minimum 4 maximum 20
# height bu sayılar oalcak sekilde
"""
4 için
   * -- 3 boşluk 1 yıldız
  *** -- 2 boşluk 3 yıldız
 ***** -- 1 boşluk 5 yıldız
******* -- boşkuk yok 7 yıldız
"""
#print("EMre"*5,"Kardelen",end="\n",sep=" ")
#print("Cihat"*5)
"""""""""
height = int(input("yükseklik giriniz :"))

for i in range(1,height+1):
        print(" "*(height-i)+"* "*i)
"""""""""
"""
height 5 için
0. satır 4 boşlık 1 yıldız 4 boşluk
1. satır 3 boşluk 3 yıldız 3 boşluk
2. satır 2 boşluk 5 yıldız 2 boşluk
3. satır 1 boşluk 7 yıldız 1 boşluk
"""
height = int(input("yükseklik giriniz :"))

for i in range(height):
        #for j in range(height-i-1):
        print(" "*(height-i-1),end="")
        print("*"*(2*i+1), end="")
        #for j in range(2*i+1):
        #        print("*",end="")


        print()



