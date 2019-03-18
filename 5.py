div_numbers = [i for i in range(2, 21)]
min_number = 1
for i in range(20, 1, -1):
    for j in range(i - 1, 1, -1):
        if i % j == 0:
            if j in div_numbers:
                div_numbers.remove(j)
            break

for n in div_numbers:
    min_number *= n
print(div_numbers)
