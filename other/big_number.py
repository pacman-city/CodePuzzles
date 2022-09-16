"""
    Задача Большое число
    Даны числа. Нужно определить, какое самое большое число можно из них составить.

    В первой строке записано n — количество чисел.
    Во второй через пробел n неотрицательных чисел.
"""

# _ = input()
# numbers = input().split()

_ = 5
numbers = '2 4 5 2 10'.split()


def comparator(val_1, val_2):
    if val_1 + val_2 > val_2 + val_1:
        return True
    return False


def insertion_sort(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and less(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


insertion_sort(numbers, comparator)
print(*numbers, sep='')  # 542210
