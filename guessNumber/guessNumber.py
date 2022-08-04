# kullanıcdan sayı almayı öğren
# random sayı alacaksın 4 haneli
# kullanıcdan sayı all
# doğru ise tebrikler.
# yanlışsa ve tahmin ettiği sayı daha büyükse Daha büyük
# yanlışsa ve tahmin ettiği küçükse daha küçük yazdır
# tahmin 4 haneli olmalı
# tahmin sayı olmalı


# fonksiyon method öğrenmiş oldun
# while döngüsü kullanımı
# Tuple öğrendik.


def checkResult(tahmin, myNumber):
    if tahmin == myNumber:
        return True, ""
    else:
        if tahmin > myNumber:
            return False, "Tutulan sayı daha küçük"
        else:
            return False, "Tutulan sayı daha büyük"


result = False
msg = ""
guess = 0
sayi1 = 5234
while not result:
    print(msg)
    try:
        guess = int(input("\nTahmininizi giriniz :"))
    except Exception as ex:
        print("Burada Hata Var Tahmin Int Olmalı")
    result, msg = checkResult(guess, sayi1)

print(sayi1, "\ntebrikler doğru bildiniz.")
