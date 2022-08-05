# kullancıdan 1 sayı al minimum 4 maximum 20
# height bu sayı oalcak sekilde
"""
4 için
******* -- 0. satırda 0 boşluk 7 yıldız
 *****  -- 1. satırda 1 boşluk 5 yıldız
  ***  -- 2. satırda 2 boşluk 3 yıldız
   *
"""
height = int(input("yükseklik giriniz :"))

for i in range(height):
        #for j in range(i):
        print(" "*i,end="")
        #for j in range(2*(height-i)-1):
        print("*"*(2*(height-i)-1),end="")

        print()