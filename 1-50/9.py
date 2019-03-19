a = 1
b = 1
c = 1
result = 0
for i in range(1, 500):
    for j in range(1, 500):
        for k in range(1, 500):
            if (i + j + k == 1000) and (i ** 2 + j ** 2 == k ** 2):
                result = i * j * k
                break
        if result:
            break
    if result:
        break
print(result)

