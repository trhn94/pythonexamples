arr=[]

for i in range(3):
    name = input("adınızı giriniz:")
    grade = int(input("notunuzu giriniz:"))
    age = int(input("yasınızı giriniz:"))
    a = {}
    a["name"]= name
    a["grade"]= grade
    a["age"]= age
    arr.append(a)
notlar=[]
for ogrenci in arr:
    print(ogrenci["name"], "=====" ,ogrenci["grade"])
    notlar.append(ogrenci["grade"])
print("ortalama === ", round(sum(notlar)/len(notlar), 1))


