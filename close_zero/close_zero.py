"""
Тимофей ищет место, чтобы построить себе дом.
Улица состоит из участков,
каждый из которых либо пустой, либо на нём уже построен дом.
Тимофей хочет жить недалеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до
ближайшего пустого участка.

Необходимо посчитать искомые расстояния.
Для этого есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте не упорядочены.
Пустые участки обозначены нулями.
"""
from typing import List, Union


# ближайший ноль
# id:
# 85831054


def get_data() -> List[int]:
    """
    Входные данные:
    '7', '0 1 2 3 4 5 0 11 12 13 14 15' - длинна улицы, улица
    улица - строка с числами, вида:
    0 _ _ _ _ _ 0 _ _ _ _ _ - где «_» - любое число, не «0»
   """
    _ = input()
    array = [int(house) for house in input().split()]
    return array


def print_data(street: List[int]):
    """
    Выходные данные:
    |0| 1 2 3 2 1 |0| 1 2 3 4 5
    строка, в которой все номера, кроме «0», заменены на
    числа - удаленность до ближайшего «0»
    """
    print(*street)


def get_index(street: List[int], start: int) -> Union[int, float]:
    """Получить индекс числа «0» или infinity"""
    try:
        return street.index(0, start)
    except ValueError:
        return float('inf')


def compose_data(street: List[int]) -> List[int]:
    """
    РАБОТА АЛГОРИТМА:
    заменяет числа в исходном массиве street(кроме нулей) на вычисленные:

    street[house_index] = min( to_prev, to_next )       [line 92]

        house_index - текущая итерация цикла
        to_prev     - «шагов» влево до «0»
        to_next     - «шагов» вправо до «0»

        На каждой итерации:
        to_prev     - возрастает   1 2 3 4 5
        to_next     - убывает      5 4 3 2 1

        если house == 0 - start over & continue:        [line 84-87]

        index_zero - индекс нуля справа от текущей итерации
    --------------------------------------------------------------------
    если array начинается не с нуля:
    to_prev = infinity - исключается из MIN             [line 81]
    array[i] = to_next

    если array заканчивается не на 0:
    to_next == infinity - исключается из MIN            [line 50, 86, 90]
    array[i] = to_prev
    """
    index_zero = get_index(street, 0)
    to_prev = float('inf')

    for house_index, house in enumerate(street):
        if house == 0:
            to_prev = 0
            index_zero = get_index(street, house_index + 1)
            continue

        to_prev += 1
        to_next = index_zero - house_index

        street[house_index] = min(to_prev, to_next)

    return street


def main():
    street_in = get_data()
    street_out = compose_data(street_in)
    print_data(street_out)


if __name__ == '__main__':
    main()
