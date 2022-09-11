"""
    Написать калькулятор.
    На вход подается выражение в обратной польской нотации.
    Обратная польская нотация http://algolist.ru/syntax/revpn.php.
    Результат выводится в консоль.
"""
from math import floor
from operator import add, sub, mul, truediv


# id 86792069

class EmptyStack(Exception):
    def __init__(self):
        super().__init__('pop from empty stack')


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise EmptyStack


def get_data():
    """Пример входных данных: 7 2 + 4 * 2 + """
    return input().split()


def calculate():
    stack = Stack()
    d = {'+': add, '-': sub, '*': mul, '/': truediv}
    try:
        for value in operand_array:
            if value in '+-*/':
                b, a = stack.pop(), stack.pop()
                stack.push(floor(d[value](a, b)))
                continue
            stack.push(int(value))
        return stack.pop()
    except EmptyStack as error:
        print(f'Произошла ошибка: {error}')


if __name__ == '__main__':
    operand_array = get_data()
    result = calculate()
    print(result)
