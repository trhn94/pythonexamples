s = int(input("Bir sayı giriniz:"))
bolenler = []
for a in range(1,s):
    if s%a==0:
        bolenler.append(a)
if sum(bolenler) == s:
    print("Bu sayi mukemmeldir.")
else:
    print("Bu sayı mukemmel degildir.")