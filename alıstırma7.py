arr = [2, 7, 24, 36, 55]
s = int(input("Bir sayı giriniz"))
i = 0
while i < len(arr):
    if arr[i] == s:
        print("Bu sayı listede var.")
        print("Bu sayı listenin  " +str(i+1)+ ". elemanıdır.")
        break
    i = i + 1
else:
    print("bulamadık")