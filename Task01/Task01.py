sp = [int(I) for I in input('Введите числа: ').split()]
print(sp)
sum = 0
for i in range(1, len(sp), 2):
    sum = sum + sp[i]
print(sum)
