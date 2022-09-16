"""
    Найти максимальный периметр треугольника из введенных чисел.

    В первой строке записано количество отрезков.
    Во второй даны длины отрезков.

    Из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник,
    если выполнено неравенство треугольника: c < a + b.
"""

# n = int(input())
# array = [int(num) for num in input().split()]

n = 6
array = [int(num) for num in '5 3 7 2 8 3'.split()]

array.sort(reverse=True)

for i in range(n - 2):
    c = array[i]
    a = array[i + 1]
    b = array[i + 2]
    if c < a + b:
        print(a + b + c)
        break
else:
    print(None)
