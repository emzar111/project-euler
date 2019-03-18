from math import sqrt


def simple_numbers(n):
    count = 0
    simple_number = 0

    if n == 1:
        simple_number = 2
        return simple_number
    if n == 2:
        simple_number = 3
        return simple_number
    while count < n:
        for i in range(5, n + 1, 2):
            if i % 5 == 0:
                continue
            for j in range(3, i + 1):
                if j > int(sqrt(i)):
                    simple_list.append(i)
                    break
                if i % j == 0:
                    break

    return simple_list
