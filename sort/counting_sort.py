def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    result = []
    for value in range(k):
        result += [value] * counted_values[value]

    return result


closet = [int(num) for num in '2 2 1 1 2 2 0 0 2 0 1 1 0 2 2 0 0 2 1 1 0 2 2 1 1 0 2 0 1 0 2 0'.split()]
sorted = counting_sort(closet, 3)
print(*sorted)
