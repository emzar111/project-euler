def sum_sqrt(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum


def sqrt_sum(n):
    return (sum(i for i in range(1, n + 1))) ** 2


print(sqrt_sum(100) - sum_sqrt(100))
