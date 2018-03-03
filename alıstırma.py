n = int(input("Bir sayı giriniz:"))
f = 1
s1 = 1
s2 = 1
arr = [s1 , s2]
while f <= n:
    f = s1 + s2
    s1 = s2
    s2 = f
    if f <= n:
        arr.append(f)
print(arr)
