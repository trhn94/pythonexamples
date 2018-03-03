numbers= [2, 3, 0, -4, 5, -13, 21]

min= numbers[0]


def find_min(numbers, min):
    for number in numbers:
        if number < min:
            min = number
    return min

minimum = find_min(numbers, min)
print(minimum)
