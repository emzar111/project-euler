import itertools as itr


def div_count(n: int):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def triangle_number(n: int):
    return sum(range(1, n + 1))


def tn_high_div(divs: int):
    for i in itr.accumulate(range(2000)):
        if div_count(i) > divs:
            return i
            break
    return -1


print(tn_high_div(500))



