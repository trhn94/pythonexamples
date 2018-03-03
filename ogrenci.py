def ogrenci_ekleme():
    name= input("adınızı giriniz:")
    grade= int(input("notunuzu giriniz:"))
    a={}
    a["name"]= name
    a["grade"]= grade
    return a
b= ogrenci_ekleme()
print(b)