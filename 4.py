num = 125
result = 0


def int_reverse(n):
    n = str(n)
    n_reverse = ''
    for i in range(len(n) - 1, -1, -1):
        n_reverse += n[i]
    return int(n_reverse)


for i in range(100000, 1000000):
    if i == int_reverse(i):
        for j in range(100, 1000):
            if i % j == 0:
                if len(str(int(i / j))) == 3:
                    result = i
print(result)








