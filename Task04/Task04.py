# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Встроенный метод
# a = int(input('Введите число: '))
# print(bin(a))

a = int(input('Введите число '))
b = ''
while a > 0:
    b = str(a%2) + b
    a = a // 2
print(b)
