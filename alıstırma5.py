s= int(input("bir sayı giriniz:"))
a=[]
a.append(s)
tercih = int(input("Devam etmek istermisiniz: (E=1 , H=0)"))
while tercih == 1:
    s= int(input("Yeni bir sayı giriniz:"))
    a.append(s)
    tercih = int(input("Devam etmek istermisiniz: (E=1 , H=0)"))
print(a)


