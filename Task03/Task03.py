# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random


a = []
b = []
for i in range(random.randint(1, 10)):
    t = float('.' + str(random.randint(1, 30)))
    a.append(float(str(random.randint(1, 10)) + str(t)))
    b.append(t)

print(a)
print(round(max(b) - min(b), 3))