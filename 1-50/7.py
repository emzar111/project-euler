from math import sqrt


def simple_number(n):

    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    i = 5
    count = 3
    s_num = 0

    while count < n:
        if i % 5 == 0:
            i += 2
            continue
        for j in range(3, i + 1):
            if j > int(sqrt(i)):
                s_num = i
                count += 1
                break
            if i % j == 0:
                break
        i += 2
    return s_num


print(simple_number(10001))
