"""
Дан неправильный массив, который получился из кольцевого буфера.
Пример:
19 21 100 101 1 4 5 7 12
кольцевой буфер был отсортирован, но его начало
не совпадает с началом полученного массива.
Необходимо написать поиск индекса в таком массиве
для заданного числа(target)


РЕШЕНИЕ:
При анализе входных данных выявлена закономерность:
Если рекурсивно разбивать массив пополам(массив - больше 2-x),
то одна из половин будет всегда правильно отсортирована,
а другая - как правильно, так и нет.

Таким образом можно применить бинарный поиск,
но проверку осуществлять по правильной стороне.
Для правильной стороны выполняется условие(для неправильной не выполняется):
left < mid | mid < right

Кроме того проверку нужно делать диапазонами:
если left <= target < mid -> значит target слева(не справа)

Изменена база рекурсии:
т.к. массив неправильный, то для массива из 2-х значений - алгоритм ломается.
Проверяем каждое значение простым условием.
"""


def binary_search(arr, target, left, right):
    # база рекурсии:
    if right <= left + 1:  # осталось 2 элемента или меньше
        for i in range(left, right + 1):
            if arr[i] == target:
                return i
        else:
            return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    # левая сторона - отсортирована:
    if arr[left] < arr[mid]:
        if arr[left] <= target < arr[mid]:  # <=, left - включаем
            return binary_search(arr, target, left, mid)  # X слева
        return binary_search(arr, target, mid + 1, right)  # иначе справа

    # правая сторона отсортирована:
    if arr[mid] < target <= arr[right]:
        return binary_search(arr, target, mid + 1, right)
    return binary_search(arr, target, left, mid)


def broken_search(nums, target):
    return binary_search(nums, target, 0, len(nums) - 1)


if __name__ == '__main__':
    array = [int(num) for num in input().split()]
    result = broken_search(array, 4)
    print(result)
