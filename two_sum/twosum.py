"""
2-SUM, или TwoSum.

Дан массив целых чисел numbers и целое число X.
Нужно найти в массиве два элемента, сумма которых равняется X.
"""

# Наивный алгоритм
def two_sum(numbers, X):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]

    return None, None  # если пара не найдена


def two_sum_with_sort(numbers, X):
    numbers.sort()  # Сортируем исходный массив стандартной функцией.

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1

    return None, None


def two_sum_with_set(numbers, X):
    previous = set()  # Создаём вспомогательную структуру данных с быстрым поиском элемента

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    return None, None


if __name__ == '__main__':
    array = [1, 4, 5, 5, 5, 7, 9, 12, 18, 15, 22, 34, 36, 38, 38, 38]
    X = 54
    print(two_sum(array, X))
    print(two_sum_with_sort(array, X))
    print(two_sum_with_set(array, X))