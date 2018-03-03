meyve=["elma", "armut", "uzum"]
fiyat=[4, 3, 5]
stok=[15, 20, 24]
fiyatlar= dict(zip(meyve,fiyat))
print(fiyatlar)
stoklar= dict(zip(meyve,stok))
print(stoklar)
maliyet= []
for key, value in fiyatlar.items():
    maliyet.append(value*stoklar[key])
print(maliyet)

maliyet= {}
for key, value in fiyatlar.items():
    m= {key: value*stoklar[key]}
    maliyet.update(m)
print(maliyet)
