from random import randrange as rr
x= rr(1,15)
a= int(input("bir tahminde bulunun:"))
while 1 <= a <= 15:
    if a == x:
         print("doğru tahmin.")
         break
    if a < x:
        print("daha büyük bir sayı giriniz")
    else:
        print("daha küçük bir sayı giriniz.")
    a= int(input("yeni bir sayı giriniz:"))
