"""
    Сортировка выбором - selection sort.

    Ищет максимальный элемент(проходит все и выбирает max())
    и помещает его на соответствующую позицию
    повторяет для остатка массива.
"""


def sort_data(a, n):
    for i in range(n - 1):
        smallest = a[i]
        index = i
        for j in range(i, n):
            if a[j] < smallest:
                smallest = a[j]
                index = j
        a[i], a[index] = a[index], a[i]


if __name__ == '__main__':
    array = [24, 17, 91, 96, 67]
    length = len(array)
    sort_data(array, length)

    print(array)
