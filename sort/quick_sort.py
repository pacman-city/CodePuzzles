def partition(array, pivot):
    povot_val = array[pivot]

    left, center, right = [], [], []
    for value in array:
        if value > povot_val:
            right.append(value)
        elif value < povot_val:
            left.append(value)
        else:
            center.append(value)
    return left, center, right


def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    else:
        pivot = len(array) // 2
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


if __name__ == '__main__':
    data = [7, 9, 0, -67, 34, 12, -3, 1, 45, 100, 6, 8, -2, 99]
    sorted = quicksort(data)
    print(sorted)
