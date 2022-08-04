import random

"""

print(random.randint(0,9))
pow(3,5)
print(divmod(10,6))      (1,4)

# ctrl  /  comment
# ctrl  alt l    reformat   dosyayı düzenler
# ctrl  d  duplicate
# ctrl  alt -   fold    collapse küçült
# ctrl  alt +   extract    aç büyüt


# if elif else  condition
# x = 10
# y = 4
# print(x // y)
# print(x / y)
# print(x % y)
# print("-----------------------")
# x = 2  # None
# if x:
#     a = 5
# elif x:
#     a = 7
# else:
#     a = 6
# print(a)
# print("-----------------------")
# a="ekrem"
# for x in a:
#     print(x)
# print("----------------------")
# a=10
# 
# for x in range(5,10,5):
#     print(x)
# print("----------------------")
# a = 2
# while a < 5:
#     print(a)
#     a += 1
"""


def isPrime(number):
    myDividers=[]
    prime=True
    for i in range(2, number):
        if (number % i) == 0:
            myDividers.append(i)
            prime=False
    return prime, myDividers


if __name__ == "__main__":
    while True:
        sayi = int(input("Sayıyı girin :"))
        result, notPrime = isPrime(sayi)
        if result:
            print(sayi, "Asal sayıdır.\n\n")
        else:
            print(sayi, "Asal sayi degildir. " , notPrime)
