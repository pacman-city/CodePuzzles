"""
«Игра тренажер»
Представляет собой поле из клавиш 4x4.
На клавише написана либо точка, либо цифра от 1 до 9:
1 2 3 1
2 . . 2
2 . . 2
2 . . 2
Для каждой новой игры обновляется конфигурация клавиатуры.
В игре 9 раундов
В каждом раунде игрок должен нажать все цифры, которые равны номеру раунда.
Если игрок смог нажать все кнопки - начисляется 1 бал.

Найдите число баллов, которое смогут заработать Пупа и Лупа,
если они работают на пилораме, но будут нажимать на клавиши вдвоём.

Входные данные:
3                       количество оставшихся пальцев(каждого)
1 2 3 1                 клавиатура
2 . . 2
2 . . 2
2 . . 2
"""
from typing import List, Tuple


# ловкость рук
# id:
# 85830496

def get_data() -> Tuple[int, List[int]]:
    """Данные из stdin - преобразовать в: int, list[int](без точек)"""
    intact_fingers = int(input()) * 2
    keyboard = [int(v) for _ in range(4)
                for v in input() if v.isnumeric()]
    return intact_fingers, keyboard


def print_data(score: int):
    print(score)


def calc_score(intact_fingers: int, keyboard: List[int]) -> int:
    score = 0
    for i in range(1, 10):
        if 0 < keyboard.count(i) <= intact_fingers:
            score += 1
    return score


if __name__ == '__main__':
    data = get_data()
    game_score = calc_score(*data)
    print_data(game_score)
