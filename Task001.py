# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#   1 2 3 4 5
#   3
#   -> 1

N = int(input('Введите количество элементов в массиве: '))

import random
numbers_ = []
for i in range(N):
    numbers_.append(random.randint(1,10))
print(numbers_)

X = int(input('Введите искомое число: '))
count = 0
for num in numbers_:
    if num == X:
        count += 1

print(f'Число {X} содержится в массиве {count} раз.')