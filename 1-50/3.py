from math import sqrt

num = 600851475143
nod_simple = 1


def simple_number(number):
    lst = [2, 3, 5]

    if number == 2:
        lst = 2
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


def is_simple(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


for i in range(3, num, 2):
    if num % i == 0:
        nod_simple = int(num / i)
        if is_simple(nod_simple):
            break
print(nod_simple)





