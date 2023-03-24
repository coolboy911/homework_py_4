# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint

n = int(input("введите кол-во элементов первой последовательности: "))
list_1 = [randint(0, 20) for _ in range(n)]
print(*list_1)
m = int(input("введите кол-во элементов второй последовательности: "))
list_2 = [randint(0, 20) for _ in range(m)]
print(*list_2)

intersection = set(list_1).intersection(set(list_2))  # создали сет с общими элементами
print(*intersection, "(общие элементы)")

intersection = list(intersection)
for i in range(len(intersection)-1):  # sorting starting from min to max
    for j in range(i+1, len(intersection)):
        if intersection[j] < intersection[i]:
            intersection[j], intersection[i] = intersection[i], intersection[j] 
print(*intersection, "(ответ задачи)")