dikey= [1,2,3,4,5,6,7,8]
yatay= ["a", "b", "c", "d", "e", "f", "g", "h"]
x = input('Yatay pozisyonu giriniz: ["a", "b", "c", "d", "e", "f", "g", "h"]   ===>   ')
y = int(input("Dikey pozisyonu giriniz: [1,2,3,4,5,6,7,8]  ===>   "))
i = yatay.index(x)
j = dikey.index(y)
positions = []


def create_positions_one(j, hor):
    if j >= 1:
        ver1 = j - 1
        positions.append((yatay[hor], dikey[ver1]))
    if j <= 6:
        ver1 = j +1
        positions.append((yatay[hor], dikey[ver1]))

def create_positions_two(j, hor):
    if j >= 2:
        ver1 = j - 2
        positions.append((yatay[hor], dikey[ver1]))
    if j <= 5:
        ver1 = j + 2
        positions.append((yatay[hor], dikey[ver1]))



def horizontal_backword(i, j):
    if i >= 2:
        hor1 = i - 2
        create_positions_one(j, hor1)
        hor2 = i - 1
        create_positions_two(j, hor2)
    elif i >= 1:
        hor2= i - 1
        create_positions_two(j, hor2)
def horizontal_forward(i, j):
    if i + 2 < len(yatay):
        hor1 = i + 2
        create_positions_one(j, hor1)
        hor2 = i + 1
        create_positions_two(j, hor2)
    elif i + 1 < len(yatay):
        hor2 = i + 1
        create_positions_two(j, hor2)
horizontal_backword(i, j)
horizontal_forward(i, j)
print(positions)