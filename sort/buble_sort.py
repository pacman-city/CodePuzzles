"""Пузырьковая сортировка на месте"""


def sort_data(a, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == '__main__':
    array = [24, 17, 91, 96, 67]
    length = len(array)
    sort_data(array, length)

    print(array)
