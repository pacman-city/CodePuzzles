def get_data():
    _ = input()
    street = [int(house) for house in input().split()]
    return street


def nearest_zero(street):
    """
        Алгоритм проходит массив street и сохраняет результат в array

        Сначала внешний цикл заполняет array значением из counter += 1

        Если house равен нулю - запускается цикл в обратном направлении
        от текущего i до counter <= array[j]
        цикл перезаписывает array от нуля назад 1 2 3 4 ...
    """
    array = [0] * len(street)
    counter = float('inf')

    for i, house in enumerate(street):
        if house == 0:
            counter = 0
            for j in range(i, -1, -1):
                if counter <= array[j]:
                    array[j] = counter
                    counter += 1
                else:
                    break
            counter = 0
        else:
            counter += 1
            array[i] = counter

    return array


street_in = get_data()
result = nearest_zero(street_in)
print(*result)
