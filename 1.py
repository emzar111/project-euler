a = 3
b = 5
sum = 0
for i in range(1,1000):
    if (i % a == 0) or (i % b == 0):
        sum += i
print(sum)
