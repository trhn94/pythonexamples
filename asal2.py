x = int(input("Bir sayı giriniz:"))
b = False
for a in range(2, x):
    if x%a==0:
       
        b = True
if b == True:
    print("Bu sayı asal degildir.")
else:
    print("Bu sayı asaldır.")