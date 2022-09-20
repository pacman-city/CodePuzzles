"""
    Даны результаты соревнований.
    В первой стоке передается n - количество участников.
    Далее идут данные каждого участника в новой строке.
    В каждой строке «login участника количество решенных задач штрафы»
    Необходимо вывести логины участников в следующем порядке:
    1 количеству решенных задач(по убыванию), если равны, то
    2 количеству штрафов(по возрастанию), если равны, то
    3 в алфавитном порядке(по возрастанию)

    Для решения задачи необходимо использовать алгоритм быстрой сортировки «на месте».
"""
from collections import namedtuple


# id: 87255310

def swap(array, left, right):
    """Меняет 2 аргумента массива местами"""
    array[left], array[right] = array[right], array[left]


def partition(array, left, right):
    pivot = array[left]
    while left != right:
        if array[left] < pivot:
            left += 1
            continue
        if array[right] > pivot:
            right -= 1
            continue
        if array[left] >= pivot >= array[right]:
            swap(array, left, right)
    return left


def quicksort(array, left, right):
    if right - left > 1:
        center = partition(array, left, right)
        quicksort(array, left, center)
        quicksort(array, center + 1, right)
    else:
        if left + 1 == right and array[left] > array[right]:
            swap(array, left, right)


def split_data(string, Participant):
    """
        Разделяет строку на аргументы и конвертирует данные в формат,
        необходимый для сортировки
    """
    login, count, fine = string.split()
    participant = Participant(count=-int(count), fine=int(fine), login=login)
    return participant


def get_data():
    """
        На вход подается n строк.
        Каждая строка состоит из:  «login count fine»
        login - имя участника
        count - количество решенных задач
        fine - количество штрафов
        :return: [Tuple(login count fine)]
    """
    participant_count = int(input())
    participants = []
    Participant = namedtuple('Participant', 'count fine login')
    for _ in range(participant_count):
        participants.append(split_data(input(), Participant))
    return participants


def print_data(participants):
    print(*[participant.login for participant in participants], sep='\n')


if __name__ == '__main__':
    competees = get_data()
    quicksort(competees, 0, len(competees) - 1)
    print_data(competees)
