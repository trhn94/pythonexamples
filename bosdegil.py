even_numbers=[]
a= int(input("bir sayı giriniz:"))
if a%2==0:
    even_numbers.append(a)
elif a%2!=0:
    print("bu sayı çift sayı değildir")
print(even_numbers)