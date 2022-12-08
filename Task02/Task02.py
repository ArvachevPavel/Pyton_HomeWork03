# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
spisok1 = [int(I) for I in input('Введите числа: ').split()]
print(spisok1)
spisok2 = []
flag1 = len(spisok1)
for i in range(len(spisok1)):
    while i < len(spisok1)/2 and flag1 > len(spisok1)/2:
        flag1 = flag1 - 1
        a = spisok1[i] * spisok1[flag1]
        spisok2.append(a)
        i += 1
print(spisok2)