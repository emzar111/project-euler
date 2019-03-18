from math import sqrt


result = 1


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


d_nums = {i: 1 for i in simple_numbers(20)}

for i in range (2, 21):
    for s in simple_numbers(i):
        if i % s == 0:
            if i // s > d_nums[s]:
                d_nums[s] = i // s

print(d_nums)

for i in d_nums.keys():
    result *= (i**d_nums[i])
print(d_nums)