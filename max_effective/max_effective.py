"""
    Реализуйте класс StackMaxEffective,
    поддерживающий операцию определения максимума среди элементов в стеке.
    Сложность операции должна быть O(1).
    Для пустого стека операция должна возвращать None.
    При этом push(x) и pop() также должны выполняться за константное время.

    В первой строке записано одно число — количество команд.
    Далее идут команды по одной в строке, следующих видов:
    push(x) — добавить число x в стек;
    pop() — удалить число с вершины стека;
    get_max() — напечатать максимальное число в стеке;
    Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».

    Решение:
    Поскольку стек поддерживает только удаление от конца массива,
    то создаем еще один массив - max - где записываем максимальное значение.
    При записи(push) проверяем если добавляемое число - больше последнего в массиве max,
    тогда в max записываем это значение - если нет - то дублируем последнее значение в max
    Таким образом длинна max и data - одинаковые
    При удалении из стека - так же удаляем одно значение из max.

    Такое решение возможно только для стека - если значения не удаляются из середины.
"""


class StackMax:
    data = []
    max = []

    @classmethod
    def push(cls, x):
        val = int(x)
        cls.data.append(val)

        m = cls.max
        if not len(m):
            m.append(val)
        elif m[-1] < val:
            m.append(val)
        else:
            m.append(m[-1])

    @classmethod
    def pop(cls):
        if not len(cls.data):
            print('error')
        else:
            cls.data.pop(-1)
            cls.max.pop(-1)

    @classmethod
    def get_max(cls):
        if not len(cls.data):
            print(None)
        else:
            print(cls.max[-1])


a = int(input())

for _ in range(a):
    b = input().split()
    if b[0] == 'push':
        StackMax.push(b[1])
    if b[0] == 'pop':
        StackMax.pop()
    if b[0] == 'get_max':
        StackMax.get_max()
