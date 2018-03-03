mukemmeller = []

for s in range(6,1000):
    bolenler = []
    for a in range(1,s):
        if s%a==0:
            bolenler.append(a)

    if sum(bolenler) == s:
        mukemmeller.append(s)
print(mukemmeller)
