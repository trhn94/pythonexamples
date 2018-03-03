n= int(input("Bir sayı giriniz:"))
f= 1
z=[]
mukemmel=[]
while f < n:
    if n%f==0:
        z.append(f)
    f= f + 1
if sum(z) == n:
    mukemmel.append(z)
    print("Bu sayı mukemmeldir")





