from math import sqrt


def simple_numbers(number):
    simple_list = [2, 3, 5]

    if number == 2:
        simple_list = [2]
        return simple_list
    if number == 3 or number == 4:
        simple_list = [2, 3]
        return simple_list

    for i in range(5, number + 1, 2):
        if i % 5 == 0:
            continue
        for j in range(3, i + 1):
            if j > int(sqrt(i)):
                simple_list.append(i)
                break
            if i % j == 0:
                break
    return simple_list


def d_count_number(number, n):
    count = 0
    while number % n == 0:
        count += 1
        if number == n:
            break
        number /= n
    return count


d_nums = {i: 0 for i in simple_numbers(20)}
result = 1

for i in range(2, 21):
    for s in simple_numbers(i):
        if d_count_number(i, s) > d_nums[s]:
            d_nums[s] = d_count_number(i, s)

for s in d_nums.keys():
    result *= s ** d_nums[s]


print(result)
