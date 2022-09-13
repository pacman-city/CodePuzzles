"""
    Алгоритм бинарного поиска.
    Массив данных должен быть отсортирован по возрастанию.
"""


def binarySearch(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
    mid = (left + right) // 2  # промежуток не пуст
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального
        return binarySearch(arr, x, left, mid)  # поиск слева
    else:
        return binarySearch(arr, x, mid + 1, right)  # поиск справа


x = 8
arr = [1, 2, 3, 6, 8, 10, 11, 25, 30, 50]
index = binarySearch(arr, x, left=0, right=len(arr))
print(index)
