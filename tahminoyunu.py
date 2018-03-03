from random import randrange


def check_guess(tahmin, sayi):
    while 1<= tahmin <=15:
        if tahmin == sayi :
            print("doğru tahmin.")
            break
        if tahmin < sayi:
            print("daha büyük bir sayı giriniz")
        else:
            print("daha küçük bir sayı giriniz.")
        tahmin=int(input("Bir tahminde bulunun:"))


def tahmin_oyunu():
    x= randrange(1,15)
    a=int(input("Bir tahminde bulunun:"))
    check_guess(a, x)

    
tahmin_oyunu()