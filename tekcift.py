def f(a):
    if a%2==0:
        return True
    else:
        return False
a= int(input("bir sayı giriniz:"))
sonuc = f(a)
if sonuc == True:
    print("bu sayı çifttir.")
else:
    print("Bu sayı tektir.")
