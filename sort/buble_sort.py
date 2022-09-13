"""
    Пузырьковая сортировка - bubble sort.
    Сортировка на месте - меняется исходный массив.
    Сложность O(n**2) - квадратичная.
"""


def sort_data(a):
    l = len(a)

    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == '__main__':
    array = [24, 17, 91, 96, 67]
    sort_data(array)
    print(array)
