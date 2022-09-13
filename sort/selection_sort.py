"""
    Сортировка выбором - selection sort.
    Сложность O(n**2) - квадратичная.
    Может быть устойчивой и неустойчивой в зависимости от реализации.
"""


def sort_data(a):
    l = len(a)

    for i in range(l - 1):
        smallest = a[i]
        index = i
        # Ищет максимальный элемент(проходит все и выбирает max()) и помещает его на соответствующую позицию
        for j in range(i, l):
            if a[j] < smallest:
                smallest = a[j]
                index = j
        a[i], a[index] = a[index], a[i]


if __name__ == '__main__':
    array = [24, 17, 91, 96, 67]
    sort_data(array)
    print(array)
