"""
    Сумма бинарных чисел
    Количество числ не ограничено
"""

from itertools import zip_longest


def get_arguments():
    """Получить аргументы для вычисления."""
    print('Введите БИНАРНОЕ число или q для завершения ввода')
    args = ()
    argument = input()
    while argument.lower() != 'q':
        args += (argument,)
        argument = input()

    return args


def zip_reversed(args):
    """
     Инвертирует строки -> zip.
    :param args: ('10', '1')
    :return: (('0', '1'), ('1', 0))
    """
    rev = (tuple(reversed(n)) for n in args)
    zipped = tuple(zip_longest(*rev, fillvalue=0))
    return zipped


def print_result(number):
    """
    :param number: (0, 0, 1)
    :print: '100'
    """
    num = reversed(number)
    print('СУММА ВВЕДЕННЫХ ЧИСЕЛ')
    print(*num, sep='')


def sum_binaries(num_tuple):
    """
    Суммирует двоичные числа

    АЛГОРИТМ:

    i          - счетчик итераций
    sum_bin    - результат(tuple)
    remaining  - 1 или 0, текущий регистр суммы
    s          - сумма в текущей итерации = over + сумма цифр текущего регистра
    over       - количество единиц, которое нужно добавить в следующий регистр суммы

    Вычисляем всех сумму цифр для текущего регистра (s).
    Находим число единиц, которое нужно добавить в следующий регистр (over).
    Находим цифру, которую необходимо поместить в текущий регистр (remaining).
    Добавляем в результат (sum_bin) текущее значение из remaining (0 или 1)
    увеличиваем счетчик

    Повторяем, пока не переберем максимальное число из полученных аргументов или over > 0

    Сумма s:
    == сумма цифр + over
    ИЛИ
    == over - если перебраны все аргументы из num_tuple
    """
    length = len(num_tuple)

    i = 0
    over = 0
    sum_bin = ()
    while over > 0 or i < length:
        s = over if i >= length else sum(int(i) for i in num_tuple[i]) + over
        over = s // 2
        remaining = s % 2
        sum_bin += (remaining,)
        i += 1

    return sum_bin


def main():
    arguments = get_arguments()
    num_tuple = zip_reversed(arguments)
    result = sum_binaries(num_tuple)
    print_result(result)


if __name__ == '__main__':
    main()
