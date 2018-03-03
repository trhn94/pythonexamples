s= int(input("Bir sayı giriniz:"))
bolenler=[]
mukemmel=[]
f = 1
while f < s:
    if s%f==0:
        bolenler.append(f)
    f = f+1
if sum(bolenler)== s:
    mukemmel.append(s)
tercih = int(input("Devam etmek istermisiniz: (E=1 , H=0"))
while tercih == 1:
    s= int(input("Yeni bir sayı giriniz:"))
    bolenler = []
    f = 1
    while f < s:
        if s % f == 0:
            bolenler.append(f)
        f = f+1
    if sum(bolenler) == s:
        mukemmel.append(s)
    tercih = int(input("Devam etmek istermisiniz: (E=1 , H=0)"))
print(mukemmel)



