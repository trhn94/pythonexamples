


def bubblesort(liste):
    numbers  = liste
    for index in range(len(numbers), 1, -1):
        print("index", index)
        for i in range(0, index-1):
            print("i", i)
            temp=numbers[i]
            if numbers[i] > numbers[i+1]:
                numbers[i]= numbers[i+1]
                numbers[i+1]= temp

    return numbers

numbers= [3, 2, 0, 21, -4, 5, -13]
x= bubblesort(numbers)

print(x)

