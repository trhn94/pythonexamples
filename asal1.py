


tercih = 1
while tercih == 1:
    s = int(input("bir sayı giriniz:"))
    bolen = 2
    b = False
    while bolen < s:
        if s%bolen == 0:
            b= True
        bolen = bolen + 1
    if b:
        print("sayı asal degil")
    else:
        print("sayı asal")
    tercih = int(input("Devam etmek istiyormusunuz: E=1 , H=0"))