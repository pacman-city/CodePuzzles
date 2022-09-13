"""
    Два велосипеда
    Вася решил накопить денег на два одинаковых велосипеда.
    У Васи есть копилка, в которую каждый день он может добавлять деньги.
    В процессе накопления Вася не вынимает деньги из копилки.
    У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

    Определить:
    Первый день, в которой Вася смог бы купить один велосипед.
    Первый день, в который Вася смог бы купить два велосипеда.

    Решение должно работать за O(log n).

    Входные данные:
    В первой строке - число дней n, когда Вася собирал копилку.
    В следующей строке n целых неотрицательных чисел в порядке возрастания.
    В третьей строке - стоимость велосипеда.

    Вывести два числа — номера дней по условию задачи.
    Если нужной суммы нет - -1
"""


def binarySearch(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money[middle] >= price and (money[middle - 1] < price or middle == 0)):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)


def get_data():
    # days = int(input())
    # money = [int(num) for num in input().split()]
    # price = int(input())
    days = 6
    money = [int(p) for p in '1 2 4 4 4 4'.split()]
    price = 3
    return days, money, price


if __name__ == '__main__':
    days, money, price = get_data()
    one_bike = binarySearch(money, price, left=0, right=days)
    two_bikes = binarySearch(money, price * 2, left=0, right=days)

    print(one_bike, two_bikes, sep=' ')
