# kullancıdan 1 sayı al minimum 5 maximum 31 tek sayı olacak sekilde.
# height bu sayılar oalcak sekilde
"""
7 için
   *        0. satır 3 boşuk 1 yıldız  3 boşluk
  ***       1. satır 2 boşluk 3 yıldız 2 boşluk
 *****      2. satır 1 boşluk 5 yıldız 1 boşluk
*******     3. satır 0 boşluk 7 yıldız 0 boşluk
 *****      4. satır 1 boşluk 5 yıldız 1 boşluk
  ***       5. satır 2 boşluk 3 yıldız 2 boşluk
   *        6. satır 3 boşluk 1 yıldız 3 boşluk
"""


def method1(h):
    top = h // 2 + 1
    bottom = h // 2
    for i in range(top):
        # for j in range(height-i-1):
        print(" " * (top - i - 1), end="")
        # for j in range(2*i+1):
        print("*" * ((2 * i + 1)), end="")

        print()
    for i in range(bottom):
        # for j in range(i):
        print("", end=" ")
        print(" " * i, end="")
        # for j in range(2*(height-i)-1):
        print("*" * ((2 * (bottom - i) - 1)), end="")

        print()


def method2(h):

    for i in range(h):
        # for j in range(height-i-1):
        print("-" * (abs(i-(height//2))), end="") #abs mutlak deger alır absolute O(n)  O(1) O(n^5.log(n)) complexity
        # for j in range(2*i+1):
        print("*" * ((2 * (abs(i-height//2)) + 1)), end="")## todo Burada Hata var
        print()


height = int(input("yükseklik giriniz :"))

type = 1
if type == 1:
    method1(height)
elif type == 2:
    method2(height)
