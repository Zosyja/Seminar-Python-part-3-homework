# Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
5
#  1 2 3 4 5
#  6
#   -> 5

N = int(input('Введите количество элементов в массиве: '))

import random
numbers_ = []
for i in range(N):
    numbers_.append(random.randint(1,10))
print(numbers_)

X = int(input('Введите число Х: '))
min = abs(X-numbers_[0])
index = 0
count = 1

for el in range(1,N):
    num = abs(X-numbers_[el])
    if num < min:
        min = num
        index = el
    elif num == min:
        count += 1
if count == 1:
    print(f'Самый близкий по величине к числу {X} является элемент: {numbers_[index]}')
if count > 1:
    print(f'Самыми близкими по величине к числу {X} являются элементы: {X-min} и {X+min}')