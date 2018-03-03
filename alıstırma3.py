s1= int(input("Bir sayı giriniz:"))
s2= int(input("Bir sayı giriniz:"))
f=1
arr=[]
while f < s1 and  f < s2:
    if s1%f==0 and s2%f==0:
        arr.append(f)
    f= f + 1
print(arr)
