"""Сортировка простыми вставками - insert sort"""


def sort_data(a, n):
    for i in range(1, n):
        elem = a[i]  # первый элемент из неотсортированной части списка
        j = i
        while j >= 1 and a[j - 1] > elem:
            a[j] = a[j - 1]  # перезаписывает предыдущий в следующий
            j -= 1
        a[j] = elem  # когда место найдено вписывает значение


if __name__ == '__main__':
    array = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
    length = len(array)
    sort_data(array, length)

    print(array)
