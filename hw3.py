s = int(input("Bir sayı giriniz:"))
f = 2
while s >= 1:
        if s%f==0:
            print("Bu sayı asal degildir.")
            f = f + 1
        else:
           print("Bu sayı asaldır.")
        tercih = int(input("Yeni bir sayı girmek istermisiniz: E=1 , H=0"))
        while tercih == 1:
            s = int(input("Yeni bir sayı giriniz:"))
            f = 2
            if s%f==0:
                print("Bu sayı asal degildir.")
                f = f + 1
            else:
                print("Bu sayı asaldır.")






