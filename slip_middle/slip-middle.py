"""
 Метод скользящего среднего - используется для сглаживания данных на графике

Работа метода: создаётся новый массив данных, и в нём значение каждой точки высчитывается как
среднее арифметическое предыдущих «K» значений из исходного набора.
То есть для каждого значения массива считаем среднее арифметическое из соседних значений.
"""


# Наивный алгоритм:
def moving_average(timeseries, K):
    """Вычисляем среднее на каждой итерации цикла"""
    result = []

    for begin_index in range(0, len(timeseries) - K + 1):
        end_index = begin_index + K  # Просматриваем окно шириной K

        current_sum = 0
        for v in timeseries[begin_index:end_index]:
            current_sum += v
        current_avg = current_sum / K
        result.append(current_avg)
    return result


# быстрый алгоритм
def moving_average2(timeseries, K):
    """Вычисляем среднее один раз, потом из него вычитаем предыдущее и прибавляем следующее"""
    result = []

    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)  # Первый раз вычисляем значение честно и сохраняем результат.
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


if __name__ == '__main__':
    array = [4, 3, 8, 1, 5, 6, 3]
    K_window = 3
    print(moving_average(array, K_window))
    print(moving_average2(array, K_window))
