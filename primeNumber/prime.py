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


sayi=int(input("Sayıyı girin :"))
if sayi > 1:
    for i in range(2,sayi):
        if(sayi%i)==0:
            print(sayi,"Asal sayi degildir.")
            break
        else:
            print(sayi,"Asal sayıdır.")
    else:
        print(sayi,"Asal sayı degildir.")





