"""
Объединить 2 массива в один,
где значения массивов расположены в таком порядке:
array_1 array_2 array_1 array_2
"""


def get_data():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [1, 2, 3, 4, 5]
    return list_1, list_2


def print_data(array):
    """output: 1 1 2 2 3 3 4 4 5 5"""
    print(*array)


def compose_array(list_1, list_2):
    return [x for pair in zip(list_1, list_2) for x in pair]


def main():
    data = get_data()
    array = compose_array(*data)
    print_data(array)


if __name__ == '__main__':
    main()
