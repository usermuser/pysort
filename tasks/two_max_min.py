"""Задача:В массиве чисел найти два максимальных элемента.
При этом они могут быть равны между собой или не равны.

input: [4,7,2,6,9]
output: 7,9

input: [2,4,6,8,1,3,5,7,8]
output: 8,8

#1 Оба максимума ищутся в одном цикле
      Время     Память     Модификация
#1    O(n)      O(1)        No
"""

data1 = [4, 7, 2, 6, 9]
data2 = [2, 4, 6, 8, 1, 3, 5, 7, 8]


def two_max(data):
    length = len(data)
    max1 = 0
    max2 = 1  # max2 должно быть больше чем max1 по условию задачи
    if data[max1] > data[max2]:
        max1 = 1
        max2 = 0
    for i in range(2, length):
        if data[i] > data[max1]:
            max1 = i
        if data[max2] < data[max1]:
            max1, max2 = max2, max1

    return data[max1], data[max2]


if __name__ == '__main__':
    assert two_max(data1) == (7, 9), f'Wrong solution!, result = {two_max(data1)}'
    assert two_max(data2) == (8, 8), f'Wrong solution!, result = {two_max(data2)}'
