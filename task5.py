# Реализуйте алгоритм перемешивания списка.

import random

def mix_list(list_original):
    list = list_original[:]
    length = len(list)
    for i in range(length):
        index = random.randint(0, length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

list = [1, 2, 3, 4, 5]
mixed_list = mix_list(list)

print(f'Заданный список: - {list}')
print(f'Перемешанный список: - {mixed_list}')
