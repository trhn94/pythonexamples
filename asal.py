s = int(input("Bir sayı girniz:"))
bolen = 2
while bolen < s:
    if s%bolen == 0:
        print("Bu sayı asal degildir.")
        break
        bolen = bolen + 1