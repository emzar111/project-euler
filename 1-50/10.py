from math import sqrt

result = 5
n = 5


def simple_numbers(number):
    lst = [2, 3, 5]

    if number == 2:
        lst = [2]
        return lst
    if number == 3:
        lst = [2, 3]
        return lst

    for i in range(5, number + 1, 2):
        if i % 5 == 0:
            continue
        for j in range(3, i + 1):
            if j > int(sqrt(i)):
                lst.append(i)
                break
            if i % j == 0:
                break
    return lst


print(sum(simple_numbers(2000000)))

